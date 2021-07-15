
import pandas as pd
import requests
from bs4 import BeautifulSoup 

response = requests.get("http://www.rj.gov.br/Agenda.aspx")

doc = BeautifulSoup(response.text, 'html.parser')

itens = doc.select('.noticias-wrap .noticia-3col')

rows = []

for item in itens[:100]:
    row = {}
    row['dia'] = item.select('h1')[0].text
    text = ''
    description = item.findAll('p')
    for element in description:
        text += ''.join(element.findAll(text = True))
    row['descricao'] = text
    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv('agenda.csv')


