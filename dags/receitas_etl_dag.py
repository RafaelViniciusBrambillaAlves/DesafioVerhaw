# Importando bibliotecas
import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
from source.web_scraper import download_receitas
from source.data_processor import load_and_process_data
from source.organize import organize_files
from source.send_to_api import send_data_to_api

def process_send_data() -> None:
    """
    Função para organizar, processar e enviar os dados 
    """
    # Processa os dados
    resultado = load_and_process_data()
    
    # Dicionário final
    dic = {
        "Autor": "Rafael Vinicius Brambilla Alves",
        "data atual": datetime.datetime.now().strftime("%Y%m%d"),
        "Dados": resultado
    }   

    # Converte para JSON
    dic_json = json.dumps(dic, ensure_ascii=False)
    print(dic_json)

    # Envia os dados para a API
    send_data_to_api(dic_json)

# Argumentos padrão
default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2024, 9, 2),
    'retries': 1,
}

with DAG(
    dag_id='receitas_dag',
    default_args=default_args,
    description='Enviar dados do Portal para API',
    schedule_interval='0 10 * * *',  # Rodar diariamente as 10:00
    catchup=False,
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

    # Tarefa para processar os dados e enviar para a API
    process_data_task = PythonOperator(
        task_id='process_send_data',
        python_callable=process_send_data,
    )

    # Definir a ordem das tarefas na DAG
    download_task >> organize_task >> process_data_task 
