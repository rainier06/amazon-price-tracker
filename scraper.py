import random
import time
import requests
from bs4 import BeautifulSoup

url="https://www.amazon.in/dp/B09QH2LM2X"
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
# url='https://www.amazon.com/gp/product/B004JKNYL4'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle").text

print(title.strip())