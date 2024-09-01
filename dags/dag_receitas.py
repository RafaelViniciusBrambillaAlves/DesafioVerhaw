# Importando bibliotecas
from airflow import DAG
from airflow.operators.python import PythonOperator
from source.web_scraper import download_receitas
from source.data_processor import load_and_process_data
from source.organize import organize_files
import datetime
import json
from airflow.utils.dates import days_ago

def process_data():
    # Organiza os arquivos
    organize_files()
    
    # Processa os dados
    resultado_json = load_and_process_data()
    
    # Dicionário final
    dic = {
        "Autor": "Rafael Vinicius Brambilla Alves",
        "data atual": datetime.datetime.now().strftime("%Y%m%d"),
        "Dados": resultado_json
    }

    # Converte para JSON
    dic_json = json.dumps(dic, ensure_ascii=False)
    print(dic_json)

# Definir argumentos padrão para a DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Inicializa a DAG
with DAG(
    dag_id='receitas_dag',  # Novo nome da DAG
    default_args={"start_date": datetime.datetime(2023, 8, 31)},
    description='DAG para baixar receitas do Portal da Transparencia e processar dados',
    # schedule_interval='2 14 * * *',
    schedule_interval='*/3 14 * * *',  # Rodar a cada 3 minutos a partir das 14:00 UTC
    start_date=datetime.datetime(2023, 8, 31, 14, 5),   
    catchup=False
) as dag:
       
    # Tarefa para baixar receitas
    download_task = PythonOperator(
        task_id='download_receitas',
        python_callable=download_receitas,
    )

    # Tarefa para organizar arquivos
    organize_task = PythonOperator(
        task_id='organize_files',
        python_callable=organize_files,
    )

    # Tarefa para processar os dados
    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )

    # Definir a ordem das tarefas na DAG
    download_task >> organize_task >> process_data_task
