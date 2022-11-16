# Projeto Imigrantes


- Projeto que visa testar os conhecimentos adquiridos em Apache Airflow
- Análise preliminar do dataset sobre imigração no Brasil (2022)
- Exportação do resultado da subpasta pesquisa para o PostgreSQL

## Tecnologias empregadas


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
