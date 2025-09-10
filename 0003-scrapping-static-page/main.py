import csv

import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")


quote = soup.find("div", class_="quote")

with open('quotes.csv', "a+", newline='', encoding="utf-8") as f:
  writer = csv.writer(f)
  for quote in soup.select(".quote"):
    texto = quote.select_one(".text").get_text()
    autor = quote.select_one(".author").get_text()
    print(f"{texto} — {autor}")
    writer.writerow([texto, autor])
    
