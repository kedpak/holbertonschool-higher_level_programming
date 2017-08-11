#!/usr/bin/python3
"""
module select_states:
lists all states passed into argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    query = """SELECT * FROM states WHERE
    name LIKE '%s' ORDER BY id ASC;""" % sys.argv[4]
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    for i in result:
        print(i)
    cursor.close()
    db.close()
