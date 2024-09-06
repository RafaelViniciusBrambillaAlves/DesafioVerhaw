# Importando bibliotecas
from airflow import DAG
from airflow.operators.python import PythonOperator
from source.web_scraper import download_receitas
from source.data_processor import load_and_process_data
from source.organize import organize_files
import datetime
import json
import requests
from airflow.utils.dates import days_ago

# Função para enviar os dados para a API
def send_data_to_api(dic_json, url: str = "https://devbunnycofco.azurewebsites.net/acontador.aspx") -> None:
    """
    Envia os dados para a API através de um POST.

    :param dic_json: Dicionário de dados a ser enviado (formato JSON).
    :param url: URL da API onde os dados serão enviados. O valor padrão é a URL fornecida.
    """

    # Cabeçalhos da requisição
    headers = {'Content-Type': 'application/json'}
    
    try:
        # Envia a requisição POST
        response = requests.post(url, headers=headers, data=dic_json)
        response.raise_for_status()  # Levanta um erro para respostas de erro HTTP
        print(f"Dados enviados com sucesso: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar dados: {e}")