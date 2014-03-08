import sqlite3 as lite
import sys
def check_id(id):
    con = lite.connect('celery_db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT * FROM results WHERE task_id = '+str(id))
    try:
    	return cur.fetchall()
    except:
        print "no exist"

print check_id(sys.argv[1])
