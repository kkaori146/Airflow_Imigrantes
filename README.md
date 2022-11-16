# Projeto Imigrantes


- Projeto que visa testar os conhecimentos adquiridos em Apache Airflow
- Análise preliminar do dataset sobre imigração no Brasil (2022)
- Exportação do resultado da subpasta pesquisa para o PostgreSQL

## Fonte

- Portal de Imigração (Ministério da Justiça e Segurança Pública)

__https://portaldeimigracao.mj.gov.br/pt/__

## Comandos

- Implementação das modificações no docker-compose.yaml (PostgreSQL)

docker-compose up -d --no-deps --build postgres

- Solucionando problema no import do PostgresOperator no VsCode

pip install 'apache-airflow[postgres]

- Inicialização rápida do Airflow

docker-compose up airflow-init

- Implementação das modificações feitas no arquivo de extensão .py e docker-compose.yaml

docker-compose up

- Para todos os serviços associados à configuração do docker-compose que estão rodando

docker-compose down

![dependencias](https://user-images.githubusercontent.com/83531935/202231169-2b93ed3d-0db9-492c-b0a7-6a5d64f43006.png)
![pg4](https://user-images.githubusercontent.com/83531935/202231177-9ab74fa2-712f-4cbe-9cf9-c1435d1af5ad.png)

## Apache Airflow

- Dependências



##PostgreSQL

- Vista geral dos Resultados
