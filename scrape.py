import requests
from bs4 import BeautifulSoup

response = requests.get('https://coinmarketcap.com')

parsedHtml = BeautifulSoup(response.content, 'html.parser')

table = parsedHtml.find('tbody')
rows = table.find_all('tr')

for row in rows:
  target = row.find(class_='cLgOOr')
  print(target.text)

# print(rows[0])