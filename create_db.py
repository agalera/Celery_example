import sqlite3 as lite

con = lite.connect('celery_db.sqlite3')

cur = con.cursor()
cur.execute("CREATE TABLE result(Id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)")
con.commit()
