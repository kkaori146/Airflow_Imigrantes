from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
import pandas as pd
import requests
from zipfile import ZipFile
import zipfile
from io import BytesIO

#Função para extrair dados:
def extrair_dados():
  #os.makedirs("dadosbrutos/extraidos", exist_ok=True)
  url = "https://portaldeimigracao.mj.gov.br/images/Obmigra_2020/OBMigra_2022/MICRODADOS/HARMONIZADA/RAIS_CTPS_CAGED_out2022.zip"
  response = requests.get(url, verify=False) 
  open('dadosbrutos/RAIS_CTPS_CAGED_out2022.zip', 'wb').write(response.content) 
  filebytes = BytesIO(
      requests.get(url, verify=False).content
  )
  minhaExtracao = zipfile.ZipFile(filebytes)
  minhaExtracao.extractall("dados_brutos")

# Função para Leitura do Dataset Original e Tratamento:
def leitura_dados():
  df = pd.read_csv('dados_brutos/RAIS_CTPS_CAGED_2022_EXC.csv', sep=";")
  df = df.drop(['valorsalariofixo', 'unidadesalariocodigo', 'tipomovimentacao', 'indtrabintermitente', 'indtrabparcial', 'racacor', 'saldomovimentacao', 'continente', 'subclasse', 'secao', 'cbo2002ocupacao'], axis=1)
  df.rename(columns = {
  'competenciamov': 'competencia',
  'faixa_horas_contrat': 'carga_horaria_do_contrato'}, inplace=True)

  # Formatando 2 números depois da vírgula
  df.loc[:, "salario"] = df["salario"].map('{:.2f}'.format)

  # Mudança de ponto por vírgula
  df['salario'] = df['salario'].apply(lambda x: x.replace('.', ','))

  # Padronizando o formato das informações
  df['status_migratorio'] = df['status_migratorio'].apply(lambda x: x.replace('Refugiado/solicitante de refúgio', 'Refugiado/Solicitante de Refúgio'))
  df['status_migratorio'] = df['status_migratorio'].apply(lambda x: x.replace('Sem informação', 'Sem Informação'))

  # Tratamento das inconsistências
  df.replace(["NaN", "nan", " ", "", "NAN", "NA"], pd.NA, inplace = True)
  return df

def exportacao_dados(**kwargs):
  ti=kwargs['ti']
  df = ti.xcom_pull(task_ids='leitura_dados')
  
  # Conversão do dataset em arquivos csv e parquet
  df.to_csv('dadostratados/imigrantes.csv',index=False)
  df.to_parquet('dadostratados/imigrantes.parquet', index=False)

def total_paises():
  dfcsv = pd.read_csv('dadostratados/imigrantes.csv', sep=",")
  dfcsv = dfcsv.groupby(['status_migratorio', 'pais']). size().reset_index(name='total_de_imigrantes')
  # Armazenamento em formato csv
  dfcsv.to_csv('dadostratados/pesquisa/total_imigrantes.csv',index=False)

# Função para inserir dados na tabela sql a partir do dataset tratado
def inserir_dados_sql():
  dfinal = pd.read_csv('dadostratados/pesquisa/total_imigrantes.csv', sep=',')
  valores = []
  for i in range(len(dfinal)):    
    status_migratorio = dfinal.iloc[i,0]
    pais = dfinal.iloc[i,1]
    total_de_imigrantes = dfinal.iloc[i,2]
    valores.append("('%s', '%s', %s)" %(status_migratorio, pais, total_de_imigrantes))

  values = str(valores).strip('[]')
  values = values.replace('"', '')
  query = "INSERT INTO TB_IMIGRANTES(status_migratorio, pais, total_de_imigrantes) VALUES %s;" %(values)
  return query



# Definindo alguns argumentos básicos
default_args = {
    'owner':'kkaori146',
    'start_date': datetime(2022,11,7),
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay': timedelta(minutes=1)
}

#Criando a DAG:
with DAG(
    'testeimigrantes',
    max_active_runs=1,
    schedule_interval="@daily",
    default_args = default_args,
    template_searchpath= '/opt/airflow/sql') as dag:

  extrair_dados = PythonOperator(
      task_id = 'extrair_dados',
      python_callable = extrair_dados
  )

  leitura_dados = PythonOperator(
    task_id = "leitura_dados",
    python_callable= leitura_dados
  )

  exportacao_dados = PythonOperator(
    task_id = 'exportacao_dados',
    provide_context = True,
    python_callable=exportacao_dados
  )

  total_paises = PythonOperator(
    task_id = 'total_paises',
    python_callable=total_paises
  )

  criar_tabela = PostgresOperator(
    task_id = 'criar_tabela',
    postgres_conn_id = 'postgres_airflow',
    sql = 'criar_tabela.sql'
  )

  insere_dados_tabela = PostgresOperator(
    task_id = 'insere_dados_tabela',
    postgres_conn_id = 'postgres_airflow',
    sql = inserir_dados_sql()
  )
  
extrair_dados >> leitura_dados >> exportacao_dados >> total_paises >> criar_tabela >> insere_dados_tabela