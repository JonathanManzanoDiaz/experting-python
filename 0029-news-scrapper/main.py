from bs4 import BeautifulSoup
import requests

url = "https://www.20minutos.es/nacional/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    print(link.get("href"))