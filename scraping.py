from bs4 import BeautifulSoup
import requests
import re
import sys
# permitir todos caracteres
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://nulledbb.com/forum-Computing?page=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

dict_forum = {'titulo': [], 'autor': [], 'data': [], 'conteudo': []}

site = requests.get(url, headers=headers)   # <Response [200]>
soup = BeautifulSoup(site.content, 'html.parser')   # Html do site
pag = soup.find('ul', class_=re.compile(
    'd-flex flex-row align-items-center m-0 p-0'))
last_pag = pag.find_all('li')[-1].get_text()

for i in range(1, int(last_pag) + 1):  # paginas que devem ser paginadas (int(last_pag) + 1)
    url_pag = f'https://nulledbb.com/forum-Computing?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    foruns = soup.find_all('article')
    print('pag', i)

    for forum in foruns:
        tit = forum.find('div', class_=re.compile(
            'thread-title font-weight-bold'))
        titulo = tit.get_text()
        subt = forum.find('div', class_=re.compile(
            'thread-info font-size-07')).get_text()
        div = subt.split(", ")
        autor = div[0][3:]
        data = div[1]

        dict_forum['titulo'].append(titulo)
        dict_forum['autor'].append(autor)
        dict_forum['data'].append(data)

        link = tit.find('a')['href']
        url_pag_cont = f'https://nulledbb.com/{link}'
        site_cont = requests.get(url_pag_cont, headers=headers)
        soup_cont = BeautifulSoup(site_cont.content, 'html.parser')
        content = soup_cont.find('div', class_=re.compile(
            'post-message flex-fill')).get_text()
        dict_forum['conteudo'].append(content)


print(dict_forum)
