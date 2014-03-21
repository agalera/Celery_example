from celery import Celery
import sqlite3 as lite
import time
app = Celery('worker2', broker='amqp://guest@localhost//')
                                                                                                                                      
def add_result(id, value):
    while True:
        try:
            con = lite.connect('celery_db.sqlite3')
            cur = con.cursor()
            cur.execute("INSERT INTO results (task_id, result) VALUES("+str(id)+",'"+str(value)+"')")
            con.commit()
            break
        except:
            print "no puedo insertar, db bloqueada"
            time.sleep(1)
                                                                                                                                      
@app.task(queue='nivel2')
def add(id, lista):
    print "Nivel_2 init task"
    resultado = 0
    for value in lista:
        resultado += value
    add_result(id, str(resultado))
    print "Nivel_2 end task"
    return True
