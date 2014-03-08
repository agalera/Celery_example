import sqlite3 as lite

con = lite.connect('celery_db.sqlite3')

cur = con.cursor()
cur.execute("CREATE TABLE tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, actual INTEGER, total INTEGER)")
cur.execute("CREATE TABLE results(task_id INTEGER, result TEXT)")
con.commit()
