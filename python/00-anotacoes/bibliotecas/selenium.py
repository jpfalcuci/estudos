# selenium
# pip install selenium
# usado para automatizar ações no navegador web

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

user = 'user'
senha = 'senha'

servico = Service(ChromeDriverManager().install())  # coleta o último driver do Chrome
navegador = webdriver.Chrome(service=servico)       # inicia o navegador


navegador.get('https:linkdapagina.com') # acessando a página
time.sleep(0.5)

xpath = 'acessar navegador, inspecionar, encontrar elemento, clicar com direito, copy, copy xpath (realizar o processo novamente para cada elemento)'
navegador.find_element('xpath', xpath).click()
time.sleep(0.5)     # em algumas situações é necessário definir uma pausa para que o navegador carregue a página seguinte com as informações

navegador.find_element('xpath', xpath).send_keys(user)
navegador.find_element('xpath', xpath).send_keys(senha)
time.sleep(0.5)

xpath = 'xpath de algum elemento de tabela'
dados = navegador.find_element('xpath', xpath)
html = dados.get_attribute('innerHTML')

xpath = 'xpath do botão de logout'
navegador.find_element('xpath', xpath).click()
time.sleep(1)
navegador.close()   # encerra o navegador

import pandas as pd
df = pd.read_html(html) # cria um DF a partir das informações coletadas da página
