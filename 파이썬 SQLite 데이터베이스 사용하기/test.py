import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name    TEXT,
    price INTEGER)""")
conn.commit()

cur = conn.cursor()
data = [("A-item", 7700), ("B-item" , 4000), ("C-item", 8000),
        ("D-item",9400), ("E-item", 7000), ("F-item", 4000)]
cur.executemany("INSERT INTO items(name,price) VALUES(?,?)",data)
conn.commit()

cur = conn.cursor()
price_range = (4000, 7000)
cur.execute("SELECT * FROM items WHERE price>=? AND price<=?",price_range)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)