# 파이썬 SQLite 데이터베이스 사용하기

import sqlite3

->SQLite는 파이썬의 표준라이브러리 입니다 (설치가 필요없습니다 선언만 하면 됩니다)

SQLite의 장점으론 가볍고 웹브라우저 내부에서도 사용가능하며 안드로이드/iOS의 표준으로 제공하는 데이터베이스라는 것 입니다

또한 별도의 데이터베이스 애플리케이션을 사용하지 않아도 됩니다

dbpath = "test.sqlite"

conn = sqlite3.connect(dbpath)

->dbpath 변수에 test.sqlite 라는 문자열을 저장합니다 (데이터베이스 파일의 경로)

 sqlite3.connect(dbpath) 는 데이터베이스를 연결하는 동작을 합니다

----------------------------------------------------------------------------------------------------

*데이터베이스 테이블을 생성하는 함수

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS items")

cur.execute("""CREATE TABLE items (

item_id INTEGER PRIMARY KEY,

name TEXT,

price INTEGER)""")

conn.commit()

->SQLite는 데이터베이스 조작언어인 SQL을 사용합니다

conn.cusor()의 conn은 위에서 선언한 변수이고 cusor()는 데이터베이스를 조작하는 커서를 추출하는 역할을 합니다

데이터베이스에 접근할때는 cusor()를 먼저 사용해야합니다

execute()는 SQLite에 ()안에있는것을 전송하는 역할을 한다

DROP TABLE IF EXISTS items은  만약 items라는 테이블이 이미 존재한다면 삭제하라는 명령입니다

CREATE TABLE items 은 items이라는 테이블을 생성하는 명령어입니다

테이블에 item_id, name, price를 만들었습니다

변경후 conn.commit()을 해줘야 해당 설정이 반영됩니다

----------------------------------------------------------------------------------------------------

cur = conn.cursor()

data = [("A-item", 7700), ("B-item" , 4000), ("C-item", 8000),

("D-item",9400), ("E-item", 7000), ("F-item", 4000)]

cur.executemany("INSERT INTO items(name,price) VALUES(?,?)",data)

conn.commit()

-> data에 SQLite 데이베이스에 넣을 정보를 넣습니다

cur.executemany("INSERT INTO items(name,price) VALUES(?,?)",data)

-> data에 들어가있는 정보를 SQLite에 입력합니다 

----------------------------------------------------------------------------------------------------

cur = conn.cursor()

price_range = (4000, 7000)

cur.execute("SELECT * FROM items WHERE price>=? AND price<=?",price_range)

fr_list = cur.fetchall()

for fr in fr_list:

print(fr)

-> 데이터베이스내 price_range()의 숫자범위를 충족하는 price를 추출하고 그것을 출력합니다
