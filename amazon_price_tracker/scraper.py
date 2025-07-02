import requests
from bs4 import BeautifulSoup

# Your product URL
URL = "https://www.amazon.com/dp/B08N5WRWNW"  # Use a real product URL

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# Extract title
title = soup.find(id="productTitle")
if title:
    title = title.get_text(strip=True)
else:
    title = "Title Not Found"

# Extract price
price = soup.find('span', class_="a-offscreen")
if price:
    price = price.get_text(strip=True)
else:
    price = "Price Not Found"

print(f"Product: {title}")
print(f"Price: {price}")
