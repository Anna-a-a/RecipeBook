import sqlite3


conn = sqlite3.connect('recipe_book.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   login TEXT,
   password TEXT);
""")

cur.execute("""INSERT INTO users(userid, login, password) 
   VALUES('00001', 'Anna', 'qwerty');""")
conn.commit()
