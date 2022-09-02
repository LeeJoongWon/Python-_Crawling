from bs4 import BeautifulSoup
import urllib.request as req
 
url = "https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0"
res = req.urlopen(url)
 
soup = BeautifulSoup(res, "html.parser")
 
new_list = soup.select("a.news_tit")
 
for a in new_list:
    title = a.text
    href= a['href']
    print("-", title, href)
