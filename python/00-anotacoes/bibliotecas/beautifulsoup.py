# BeautifulSoup
# pip install beautifulsoup4
# transforma objetos importados de url em objetos navegaveis de forma mais simples
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

# para páginas com proteção:
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
url = 'https://www.siteprotegido.com.br'
# acessar 'devtools' no navegador, 'network', atualizar a página, acesar o arquivo 'index', menu 'headers', 'request headers' e copiar conteúdo de 'user-agent'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    print(response.read())
except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)

response = urlopen('url')
html = response.read()                      # lê o arquivo html, porém desorganizado; type(html) => bytes
html = html.decode('utf-8')                 # type(html) => str
def trata_html(html):
    return ' '.join(html.split()).replace('> <', '><') 
# transforma o html em uma lista, sem caracteres especiais; une os itens da lista com espaço ' '; elimina espaços em branco entre as tags
html = trata_html(html)

soup = BeautifulSoup(html, 'html.parser')   # devolve o html estruturado; objeto 'bs4.BeautifulSoup
soup.find('h1', id='id').get_text()         # devolve o conteúdo da tag <h1> com id='id'
print(soup.prettify())                      # mostra uma visualização formatada do html

soup.title                                  # retorna o primeiro <title> encontrado
soup.html.head.title                        # retorna o <title> dentro de <head>, dentro de <html>
soup.get_text()                             # retorna todo texto, sem tags
soup.title.get_text()                       # retorna o conteúdo da tag <title>
soup.get_text(separator=' | ', strip=True).split(' | ') # retorna o conteúdo, separado por ' | '
soup.img.attrs                              # retorna um dict com os atributos da tag <img>
soup.img.attrs.keys()                       # retorna as chaves do dicionário
soup.img.attrs.values()                     # retorna os valores do dicionário
soup.img['class']                           # retorna o valor do atributo 'class' da tag <img>
soup.img.get('src')                         # retorna o valor do atributo 'src' da tag <img>
soup.img.attrs['src']                       # outra forma de ter o memso retorno
soup.find('img')                            # retorna o primeiro conteúdo com 'img'
soup.find_all('img')                        # retorna uma lista com os itens encontrados
soup.find_all('img')[0]                     # retorna o elemtento do índice 0, da lista com os itens encontrados
soup.find_all('img', limit=2)               # retorna uma lista com os 2 primeiros itens encontrados
soup('img')                                 # atalho para o 'find_all'
soup.findAll(['h1', 'h2', 'h3'])            # retorna os itens encontrados para os itens da lista
soup.findAll('p', {'class': 'txt-value'})   # retorna uma lista com todas as tags <p> que tenham a 'class="txt-value"'
soup.findAll('p', text='conteúdo')          # text= ou string=, procura por 'conteúdo' nas tags
soup.findAll('img', alt='Foto')             # retorna todas tags que tenham 'Foto' em alt=
soup.findAll('p', class_="txt-value")       # 'class' deve ser substituído por 'class_', por ser uma palavra reservada do python
soup.findAll(text=True)                     # retorna todos os textos encontrados dentro das tags

for item in soup.findAll('img', alt='Foto'):
    print(item.get('src'))  # retorna o conteúdo de 'src' de cada tag <img> que contenha 'Foto' em alt=

soup.find('h2').find_parent('div')          # retorna a primeira tag pai, que seja <div>, do primeiro <h2> encontrado
soup.find('h2').find_parents()              # retorna todas as tags pai do primeiro <h2> encontrado

for item in soup.findAll('h2'):
    print(item.find_parent('div'))          # retorna as tags pai que sejam <div> de todos as tags <h2>

soup.find('h2').findNextSibling()           # retorna a tag irmã seguinte
soup.find('h2').findPreviousSibling()       # retorna a tag irmã anterior
soup.find('h2').findPreviousSiblings()      # retorna todas as tags irmãs anteriores, pode receber 'limit='
soup.find('h2').findNext()                  # retorna a próxima tag
soup.find('h2').findPrevious()              # retorna a tag anterior
soup.find('h2').findAllNext()               # retorna todas as próximas tags

# visualizar imagens no jupyter notebook
from IPython.display import display, HTML
display(HTML(str(soup.find('div', {'class': 'image-card'}).img)))
display(HTML("<img src=" + soup.find('div', {'class': 'image-card'}).img.get('src') + ">"))
