# DesafioVerhaw


Este projeto tem como objetivo a extração automatizada de dados do Portal da Transparência do Governo Brasileiro, organização desses dados em arquivos CSV, processamento das informações relevantes e envio para uma API. O processo é orquestrado utilizando o Apache Airflow para garantir a execução automatizada das tarefas.

## Desafio

Este projeto foi desenvolvido como parte de um desafio técnico para uma vaga. 

## Tecnologias Utilizadas 🔨

- **Python**: Linguagem principal para scripts de extração, transformação e envio de dados. 
- **Selenium**: Biblioteca para automação de navegador utilizada na extração dos dados.
- **Pandas**: Para processamento e transformação de dados.
- **Apache Airflow**: Ferramenta de orquestração de workflows utilizada para agendar e gerenciar tarefas.
- **Docker**: Contêinerização do ambiente para facilitar a execução e replicação do projeto.
- **PostgreSQL**: Banco de dados utilizado pelo Airflow.

## Estrutura do Projeto 📚

### 1. Arquivos de Configuração

- **docker-compose.yml**: Define os serviços utilizados no projeto, como o Airflow, PostgreSQL, Selenium e os volumes compartilhados. Configura a comunicação entre os diferentes contêineres.
- **Dockerfile**: Extende a imagem base do Apache Airflow e instala as dependências listadas em `requirements.txt`.
- **requirements.txt**: Lista as bibliotecas Python necessárias, como Selenium.

### 2. Scripts de Extração e Processamento

- **web_scraper.py**: Script responsável por automatizar a navegação no Portal da Transparência e baixar o arquivo CSV de receitas. Utiliza o Selenium para controlar o navegador Chrome.
- **organize.py**: Após o download, este script organiza e renomeia o arquivo CSV baixado com a data atual, garantindo que os arquivos sejam identificados corretamente.
- **data_processor.py**: Carrega o arquivo CSV organizado, filtra as colunas relevantes e transforma os dados em um dicionário pronto para ser enviado.
- **send_to_api.py**: Contém a função para enviar os dados processados para uma API externa. Envia os dados no formato JSON utilizando uma requisição HTTP POST.

### 3. DAG do Airflow

- **receitas_etl_dag.py**: Define a DAG (Directed Acyclic Graph) do Airflow que orquestra todo o processo ETL. As tarefas incluem o download dos dados, organização dos arquivos, processamento das informações e envio para a API.
  - **Tarefa `download_receitas`**: Executa o script de extração.
  - **Tarefa `organize_files`**: Organiza o arquivo baixado.
  - **Tarefa `process_send_data`**: Processa os dados e envia para a API.

## Instruções de Uso 🏃

### 1. Clonar o Repositório

Clone o repositório em sua máquina local:

```bash
git clone https://github.com/RafaelViniciusBrambillaAlves/DesafioVerhaw.git
cd DesafioVerhaw
```

### 2. Configurar e Executar os Contêineres

Construa e inicie os serviços Docker definidos no docker-compose.yml:

```bash
docker-compose up --build
```

Isso irá iniciar os serviços do Airflow, PostgreSQL, Selenium, e o restante do ambiente necessário.

### 3. Acessar o Airflow

Acesse o Airflow Web UI através do navegador:

```
http://localhost:8080
```

Logue-se com as credenciais configuradas (usuário: airflow, senha: airflow).

### 4. Executar a DAG

No Airflow, ative a DAG receitas_dag e execute-a manualmente ou aguarde o agendamento diário.

### 5. Verificar os Resultados

Os arquivos CSV processados serão armazenados na pasta csv do contêiner, e os dados processados serão enviados para a API especificada.

## Considerações Finais

Este projeto demonstra a capacidade de automatizar um fluxo de trabalho complexo utilizando tecnologias modernas de orquestração e contêinerização. As habilidades técnicas aplicadas incluem automação de navegação web, manipulação e transformação de dados, integração com APIs e orquestração de tarefas em ambientes de contêiner.
___

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

