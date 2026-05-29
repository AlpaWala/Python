import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

book = soup.find("h3").text
price = soup.find("p", class_="price_color").text

price = price.replace("Â£", "")
price = float(price)

print("Book:", book)
print("Price:", price)

if price < 20:
    print("BUY NOW 😎🔥")
else:
    print("Too expensive 😭")