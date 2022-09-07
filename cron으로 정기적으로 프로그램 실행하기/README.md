# cron으로 정기적(주기적)으로 프로그램 실행하기

macOS와 리눅스에서는 cron이라는 데몬 프로세스로 정기적으로 프로그램을 백그라운드에서 실행 할 수 있습니다

윈도우에서는 비슷한 기능으론 작업스케줄러가((Task Scheduler) 있습니다

정기 실행은

1)로그, 백업과 같은 시스템에서 필요한 정기적인 처리나

2)데이터 수집과 같은 애플리케이션에서 필요한 정기적 처리

3)시스템이 제대로 동작하고 있는지 정지적으로 감시하는 처리

등등 정기적으로 처리할 일에 적합합니다

네이버에서 제공하는 환율정보를 정기적으로 날짜별로 저장하는 프로그램을 만들어보겠습니다 (저번에 만들어놓은 코드에서 개량을 하겠습니다)

https://leejoongwon.tistory.com/66

t = datetime.date.today()

fname = t.strftime("%Y-%m-%d") + ".txt"

with open(fname, "w", encoding="utf-8") as f:

f.write(price)

-> 이 부분만 추가되었습니다

t = datetime.date.today()

->import datetime 모듈의 기능입니다

년도/ 월/ 일,과 같이 날짜정보를 얻는 기능입니다 t에는 오늘의 날짜정보를 넣습니다

fname = t.strftime("%Y-%m-%d") + ".txt"

->fname에 오늘(프로그램이 실행된 날짜)를 txt형식으로 넣습니다


with open(fname, "w", encoding="utf-8") as f:

-> fname(txt형식)을 인코딩을 utf-8로 저장합니다

# 프로그램을 정기적(주기적)으로 실행하기

이제 cron으로 하루에 한번씩 이 프로그램을 정기실행하겠습니다

macOS와 리눅스에서는 cron을 사용하고

윈도우에서는 비슷한 기능으로 작업스케줄러가((Task Scheduler)를 사용합니다

리눅스 기준으로 설명하겠습니다

vi나 nano같은 편집기로 crontap을 수정해야됩니다

저는 nano를 사용하겠습니다(익숙하신 편집기를 사용하세요)

리눅스의 터미널을 열고 nano를 인스톨합니다

sudo apt-get install nano

그 후에 밑의 명령어를 입력하여 bash_profile을 수정합니다

(cron을 수정할 때 nano를 사용하기 위함입니다)

nano ~/.bash_profile

bash_profile에 들어왔다면 export EDITOR=nano를 입력하고

Ctrl + X 를 눌러 에디터를 닫습니다 (저장할꺼냐고 묻는다면 y를 눌러 저장합니다)

그리곤 엔터(Enter)를 눌러 터미널로 빠져나옵니다

source ~/.bash_profile를 터미널에서 입력하여 바꾼 설정을 반영합니다

source ~/.bash_profile

터미널에서 crontab -e 를 입력하여 crontab설정창으로 들어옵니다

crontab -e

crontab 설정방법

crontab 서식은 다음과 같습니다

(분) (시) (일) (월) (요일) <실행할 명령어의 경로>

예시)

매월 1일 9시 10분에 실행

10 09 01 ** /실행할 프로그램 경로

매년 1월 11일 2시 22분에 실행

22 2 11 1 * /실행할 프로그램 경로


매주 월요일 9시 5분 실행 (월-1, 화-2, 수-3, 목-4, 금-5, 토-6, 일-7)

5 09 ** 1 /실행할 프로그램 경로

저는 매일 아침 9시에 위에서 만든 환률정보를 얻는 프로그램을 실행하겠습니다

crontab에서

09*** // 환율정보를 얻는 프로그램 위치
