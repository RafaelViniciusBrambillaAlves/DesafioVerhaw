from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Função que será executada como tarefa na DAG
def print_hello():
    print("Hello, World!")

# Definição da DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),  # Define a data de início
    'retries': 1,                        # Número de tentativas em caso de falha
}

# Instância da DAG
dag = DAG(
    'hello_world',                # Nome da DAG
    default_args=default_args,     # Argumentos padrão
    description='A simple hello world DAG',  # Descrição da DAG
    schedule_interval='@daily',    # Intervalo de agendamento (aqui é diário)
)

# Definição da Tarefa
hello_task = PythonOperator(
    task_id='hello_task',          # Identificador da tarefa
    python_callable=print_hello,   # Função a ser chamada
    dag=dag,                       # DAG à qual a tarefa pertence
)

# Configuração de dependências entre tarefas
# Se você tiver mais tarefas, pode definir dependências aqui
