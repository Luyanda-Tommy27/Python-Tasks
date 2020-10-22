__author__ = 'jslvtr'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-murray-ergonomic-office-chair-black/p1919328")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = (element.text.strip()) # "£250.00"

price_without_symbol = string_price[1:] # "£250.00"

price = (float(price_without_symbol))

if price < 300:
    print("You should buy the chair!")
    print("The current price is {}".format(string_price))
else:
    print("Do not buy, it's too expensive!")

# <p class="price price--large"> £250.00 </p>

