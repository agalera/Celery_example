from celery import Celery
import sqlite3 as lite
import time
app = Celery('tasks', broker='amqp://guest@localhost//')
                                                                                                                                      
@app.task
def add(id, lista):
    print "nivel_1 init task"
    for tarea in lista:
        add_level_2.delay(id, tarea)
    print "nivel_1 finish task"
    return True
                                                                                                                                      
def add_result(id, value):
    con = lite.connect('celery_db.sqlite3')
    cur = con.cursor()
    cur.execute("INSERT INTO results (task_id, result) VALUES("+str(id)+",'"+str(value)+"')")
    con.commit()
                                                                                                                                      
@app.task
def add_level_2(id, lista):
    print "Nivel_2 init task"
    resultado = 0
    for value in lista:
        resultado += value
    time.sleep(10)
    add_result(id, str(resultado))
    print "Nivel_2 end task"
    return True
