from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import datetime

def download_receitas(downloads_dir="/home/seluser/csv"):
    
    """
    Realiza a automação da navegação no portal da Transparência para 
    baixar o arquivo de receitas e renomeá-lo.
    
    :param downloads_dir: Diretório de downloads
    """
    # Opcoes do Chrome
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Preferencias de Download
    prefs = {
        "download.default_directory": downloads_dir, # diretorio dos downloads
        "download.prompt_for_download": False, # desativa a confirmação de download do chrome
        "directory_upgrade": True, # atualizas o diretorio padrao se ja existir
        "safebrowsing.enabled": True # ativa protecao contra downloads maliciosos
    }
    options.add_experimental_option("prefs", prefs)

    # Url do Selenium
    hub_url = "http://selenium-hub:4444/wd/hub"
    # Cria nova instancia do WebDriver
    driver = webdriver.Remote(command_executor=hub_url, options=options)

    try:
        # Url especificada, Portal da Transparencia do governo
        driver.get("https://portaldatransparencia.gov.br/")
        print('Acessando o portal da Transparência')
        
        # Acessa o botão (Despesas e receitas)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "despesas-card"))
        )
        button.click()

        # Acessa o botão ( Consulta na parte de Receitas)
        consulta_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='receitas-links']//a[@href='/receitas/consulta']"))
        )
        consulta_button.click()

        # Acessa o botão ( Download )
        download_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btnBaixar"))
        )
        download_button.click()

        print("Aguardando o download...")
        time.sleep(10)

        arquivo_baixado = os.path.join(downloads_dir, f"receitas.csv")
        print(arquivo_baixado)

    finally:

        # Fecha o navegador
        driver.quit()
    
    

