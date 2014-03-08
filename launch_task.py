from tasks import add
import sqlite3 as lite

con = lite.connect('celery_db.sqlite3')
cur = con.cursor()
cur.execute("INSERT INTO result (value) VALUES('no start')")
id = cur.lastrowid
print id
con.commit()
add.delay(id,2,3)
