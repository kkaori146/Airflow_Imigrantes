# Projeto Imigrantes


- Projeto visa extrair os dados de um arquivo zipado com Apache Airflow
- Tratamento dos dados
- Análise preliminar do dataset sobre imigração no Brasil (2022)
- Exportação do resultado da subpasta pesquisa para o PostgreSQL

## Ferramentas

<div align="center">
<p float="left">
  <img src="https://user-images.githubusercontent.com/83531935/202240019-106b54cb-b397-4bcc-a29a-e8ab55dcca85.png" width="200" />
  <img src="https://user-images.githubusercontent.com/83531935/202240028-cd1716fe-dfd5-4484-a9c1-9422da702468.png" width="360" /> 
  <img src="https://user-images.githubusercontent.com/83531935/202240030-59908174-d35d-4a4f-aeb8-9622420886f9.png" width="200" />
  <img src="https://user-images.githubusercontent.com/83531935/202240035-8d3d3582-b222-472d-baa8-1ed9551f2b0e.png" width="180" />
</p>
</div>


## Fonte

- Portal de Imigração (Ministério da Justiça e Segurança Pública)

__https://portaldeimigracao.mj.gov.br/pt/__

## Comandos

- Implementação das modificações no docker-compose.yaml (PostgreSQL)

**__$\textcolor{darkgreen}{\text{docker-compose up -d --no-deps --build postgres}}$__**

- Solucionando problema no import do PostgresOperator no VsCode

**__$\textcolor{darkgreen}{\text{pip install 'apache-airflow[postgres]}}$__**

- Inicialização rápida do Airflow

**__$\textcolor{darkgreen}{\text{docker-compose up airflow-init}}$__**

- Implementação das modificações feitas no arquivo de extensão .py e docker-compose.yaml

**__$\textcolor{darkgreen}{\text{docker-compose up}}$__**

- Para todos os serviços associados à configuração do docker-compose que estão rodando

**__$\textcolor{darkgreen}{\text{docker-compose down}}$__**

## Apache Airflow

- Dependências

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/202231169-2b93ed3d-0db9-492c-b0a7-6a5d64f43006.png" width=1000px > </div>


## PostgreSQL

- Vista geral dos Resultados

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/202238571-53c7cd48-ec88-48c5-b0e5-80424727d334.png" width=1000px > </div>

<br>
<br>
<hr/>

<div align="right"><p>Novembro, 2022</p></div>
