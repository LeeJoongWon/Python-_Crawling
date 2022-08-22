#기상청 날씨 크롤링하기
beautifulsoup 라이브러리를 사용합니다

beautifulsoup의 find를 사용합니다 - 한가지 단위의 데이터 추출

#설명
from bs4 import BeautifulSoup

-> BeautifulSoup 라이브러리를 사용합니다

(HTML 및 XML 문서 를 구문 분석하기위한 Python 패키지입니다)

- 설치는 터미널에서(우분투 리눅스기준) pip3 install beautifulsoup4

----------------------------------------------------------------------------------------------------

import urllib.request as req

->urllib.request는 URL을 가져오기 위한 파이썬 모듈입니다

- as req 는 urllib.request모듈을 대신할 이름을 지정하는것 입니다 (편의성을 위해)

(req는 사용자가 마음대로 이름을 바꿔도 됩니다)

url = http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp

-> url에 접속할 http주소를 넣습니다

기상청에서 RSS를 지원합니다(XML형식)

https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp?sido=1100000000&gugun=1159000000&dong=1159068000&x=36&y=8

 
----------------------------------------------------------------------------------------------------

res = req.urlopen(url)

-> urllib.request 모듈의 urlopen기능으로 url(기상청)을 열고 res에 넣습니다

 

----------------------------------------------------------------------------------------------------

soup = BeautifulSoup(res, "html.parser")

-> BeautifulSoup라이브러리로 res에 담겨있는 url(기상청)을 html.parser으로 구조를 분석하고 soup에 넣습니다

 

----------------------------------------------------------------------------------------------------

title = soup.find("title").string

wf = soup.find("wf").string

-> 위에서 분석한 정보가 담겨있는 soup에 find로 title과 wf태그의 string(문자열)을 추출하고 각각 title과 wf에 넣습니다

(URL로 들어가서 원하는 정보의 태그를 soup.find("여기에").string 입력하면 됩니다

----------------------------------------------------------------------------------------------------

print(title)

print(wf)

<- 내용물(title, wf)를 출력합니다
