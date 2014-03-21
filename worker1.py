from worker2 import add as w2_add
from celery import Celery
import sqlite3 as lite
import time
app = Celery('worker1', broker='amqp://guest@localhost//')
                                                                                                                                      
@app.task(queue='nivel1')
def add(id, lista):
    print "nivel_1 init task"
    for tarea in lista:
        w2_add.delay(id, tarea)
    print "nivel_1 finish task"
    return True
