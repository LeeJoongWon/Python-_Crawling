# 파이썬 크롤링으로 뉴스정보 수집하기

파이썬, beautifulsoup 라이브러리 사용합니다

beautifulsoup의 select을 사용합니다 - 리스트형 (다량의 자료)

# 설명

from bs4 import BeautifulSoup

-> BeautifulSoup 라이브러리를 사용합니다

(HTML 및 XML 문서 를 구문 분석하기위한 Python 패키지입니다)

- 설치는 터미널에서(우분투 리눅스 기준) pip3 install beautifulsoup4

import urllib.request as req

->urllib.request는 URL을 가져오기 위한 파이썬 모듈입니다

- as req 는 urllib.request모듈을 대신할 이름을 지정하는것 입니다 (편의성을 위해)

(req는 사용자가 마음대로 이름을 바꿔도 됩니다)

url에 접속할 http주소를 넣습니다 (네이버에서 코로나에 대해 검색해봤습니다)

----------------------------------------------------------------------------------------------------

res = req.urlopen(url)

-> urllib.request 모듈의 urlopen기능으로 url(네이버 뉴스)을 열고 res에 넣습니다

----------------------------------------------------------------------------------------------------

soup = BeautifulSoup(res, "html.parser")

-> BeautifulSoup라이브러리로 res에 담겨있는 url(네이버 뉴스)을 html.parser으로 구조를 분석하고 soup에 넣습니다

----------------------------------------------------------------------------------------------------

new_list = soup.select("a.news_tit")

-> 위에서 분석한 정보가 담겨있는 soup에 select 기능으로 "a.news_tit"안에있는 정보를 추출하고 new_list에 정보를 넣습니다

select("태그")는 페이지내에 있는 모든 태그 를 가져오는 리스트형 입니다

구글크롬(검색엔진)기준으로 정보를 얻고자 하는 사이트에서 ctrl + shift + c 를 누르시면 해당 페이지의 html 구조를 볼 수 있습니다

(얻고자 하는 정보에 마우스로 클릭하시면 해당 정보의 html구조 위치로 이동됩니다)

----------------------------------------------------------------------------------------------------

for a in new_list:

-> new_list(위에서 얻는 정보들)에 들어있는 정보만큼 반복해라 입니다

new_list에 10개의 데이터가 들어있다면 10번만큼 반복해서 동작합니다

a 에는 new_list가 차례대로 대입됩니다

for문 안에있는

title = a.text

href= a['href']

print("-", title, href)

title = a.text는 a(안에 new_list정보가 들어있음) 안에있는 텍스트를 title에 넣어라 입니다(new_list안에 텍스트는 텍스트로 된 뉴스 타이틀이 있습니다)

href= a['href']는 a 안에있는 href를(링크주소) href에 넣어라 입니다
