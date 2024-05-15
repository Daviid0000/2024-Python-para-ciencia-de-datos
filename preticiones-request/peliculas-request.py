from bs4 import BeautifulSoup
import requests
import re

url = "https://www.themoviedb.org/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

a = soup.find_all('a')


for title in a:
  print(f"etiqueta <a>: {title}")
  print("")

  for h in title:
    h1 = soup.find_all('h1')
    # headers = soup.find_all(re.compile(r'^h\d+.*'))
    print(f"etiqueta <h1>: {h}")
    print("")

  for p in title:
    parrafo = soup.find_all('p')
    print(f"etiqueta <p>: {p}")
    print("")