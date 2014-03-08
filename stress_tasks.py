from tasks import add
import sqlite3 as lite

con = lite.connect('celery_db.sqlite3')
cur = con.cursor()
for x in range(1000):
    cur.execute("INSERT INTO tasks (actual, total) VALUES(0,2)")
    id = cur.lastrowid
    print id
    add.delay(id,[[2,3],[5,3]])
con.commit()
