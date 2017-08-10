#!/usr/bin/python3
"""
module select_states:
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db="hbtn_0e_0_usa",
                     charset="utf8")

cursor = db.cursor()
cursor.execute('SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id')
result = cursor.fetchall()
for i in result:
    print(i)
cursor.close()
db.close()
