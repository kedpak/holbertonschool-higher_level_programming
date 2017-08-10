#!/usr/bin/python3
"""
module select_states:
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='root',
                     db='hbtn_0e_0_usa')

cursor = db.cursor()
cursor.execute('SELECT * FROM hbtn_0e_0_usa.states')
result = cursor.fetchall()
for i in result:
    print(i)
