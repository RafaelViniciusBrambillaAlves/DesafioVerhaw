# Importando bibliotecas
import os
import pandas as pd
import datetime

def load_and_process_data(directory_path: str="/opt/airflow/csv") -> None:
    """
    Carrega o arquivo CSV de receitas do diretório especificado,
    seleciona colunas relevantes e converte os dados.
    
    :param directory_path: Caminho do diretório onde os arquivos CSV estão armazenados
    :return: Lista de dicionários com os dados processados ou None se não encontrar o arquivo  
    """
    # Obtém a data de hoje - "YYYYMMDD"
    hoje = datetime.datetime.now().strftime("%Y%m%d")
    nome_arquivo_hoje = f"receita_{hoje}.csv"
    
    # Verifica se o Diretorio existe
    if os.path.exists(directory_path):
        # Lista todos os arquivos
        files = os.listdir(directory_path)
        print(files)

        # Verifica o arquivo de hoje
        if nome_arquivo_hoje in files:

            arquivo_path = os.path.join(directory_path, nome_arquivo_hoje)
            
            try:
                # Le o arquivo, e cria um dataframe com as colunas selecionadas
                df = pd.read_csv(arquivo_path, delimiter=';')
                colunas_selecionadas = ['Órgão', 'Espécie', 'Orçamento Atualizado (Valor Previsto)', 'Receita Realizada (Valor Arrecadado)']
                df_selecionado = df[colunas_selecionadas]

                # Retorna dados
                return df_selecionado.to_dict(orient='records')
            except pd.errors.ParserError as e:
                print(f"Erro ao tentar carregar o arquivo: {e}")
        else:
            print(f"O arquivo para a data de hoje ({nome_arquivo_hoje}) não foi encontrado.")
    else:
        print("O diretório especificado não foi encontrado.")
    return None
