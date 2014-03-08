from celery import Celery
import sqlite3 as lite
import time
app = Celery('tasks', broker='amqp://guest@localhost//')

def update_result(id, value):
    con = lite.connect('celery_db.sqlite3')
    cur = con.cursor()
    cur.execute('UPDATE result SET value="'+value+'" WHERE ID='+str(id))
    con.commit()

@app.task
def add(id, x, y):
    update_result(id, "running")
    time.sleep(10)
    resultado = x+y
    update_result(id, str(resultado))
    return True
