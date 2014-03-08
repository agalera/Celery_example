import sqlite3 as lite
import sys
def check_id(id):
    con = lite.connect('celery_db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT * FROM result WHERE ID = '+str(id))
    try:
    	return cur.fetchall()[0][1]
    except:
        print "no exist"

print check_id(sys.argv[1])
