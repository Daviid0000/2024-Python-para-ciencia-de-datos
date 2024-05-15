import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# data = response.json()

# print(f"usfdfsd: {data}")

from bs4 import BeautifulSoup

# contents = """
# <html lang="en">
# <head>
#   <title> html desde python <title>
# </head>

# <body>

# </body>
# """

# soup = BeautifulSoup(contents, features="html.parser")

url = "https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('img', class_="dynamic-carousel__img")

for img in results:
  print(img['data-src'])