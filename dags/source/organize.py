# Importando bibliotecas
import datetime
import os

def organize_files(downloads_dir="/opt/airflow/csv"):
    """
    Organiza e renomeia o arquivo de receitas baixado.

    :param directory_path: Caminho do diretório onde os arquivos CSV estão armazenados
    """

    # Data de hoje
    hoje = datetime.datetime.now().strftime("%Y%m%d")

    # Caminho arquivo original
    arquivo_original = os.path.join(downloads_dir, "receitas.csv")
    print(arquivo_original)
    
    # Caminho no arquivo
    arquivo_novo = os.path.join(downloads_dir, f"receita_{hoje}.csv")

    # Verifica a existencia do arquivo
    if os.path.exists(arquivo_original):
        # Verifica se ja existe um arquivo com a mesma data e remove ele
        if os.path.exists(arquivo_novo):
            os.remove(arquivo_novo)
        # Renomeia o arquivo 
        os.rename(arquivo_original, arquivo_novo)
        print(f"Arquivo renomeado para: {arquivo_novo}")
    else:
        print("Arquivo de receita não encontrado para renomear.")
