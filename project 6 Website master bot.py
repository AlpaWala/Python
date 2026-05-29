import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/news")

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

for headline in headlines:
    print(headline.text)