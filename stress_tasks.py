from worker1 import add
import sqlite3 as lite

con = lite.connect('celery_db.sqlite3')
cur = con.cursor()
for x in xrange(10000):
    cur.execute("INSERT INTO tasks (actual, total) VALUES(0,2)")
    id = cur.lastrowid
    add.delay(id,[[2,3],[5,3]])
con.commit()
