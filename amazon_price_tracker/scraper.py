import requests
from bs4 import BeautifulSoup
URL = "https://www.amazon.com/dp/B0B8JZ5F7D"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "Lxml")

title = soup.find(id="productTitle")
if title:
    print(title.get_text(strip=True))

else :
    print("Title not found")


price = soup.find("span", class_="a-ofscreen")
if price:
    print(price.get_text(strip=True))
else:
    print("Price not found")


print(f"Product: {title}")
print(f"Price: {price}")