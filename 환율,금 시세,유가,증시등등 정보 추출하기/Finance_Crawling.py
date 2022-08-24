from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("a.head.usd > div.head_info > span.value").string

print("usd/krw =", price)