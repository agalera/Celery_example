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

for id in range(int(sys.argv[1]), int(sys.argv[2])):
    print id, check_id(str(id))
