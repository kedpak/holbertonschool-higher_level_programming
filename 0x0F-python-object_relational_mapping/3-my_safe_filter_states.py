#!/usr/bin/python3
"""
module select_states:
lists all states passed into argument
prevent sql injection
"""

import MySQLdb
import sys
import string

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    query = """SELECT * FROM states WHERE
    name = %s ORDER BY id ASC;"""
    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4],))
    result = cursor.fetchall()

    for i in result:
        print(i)
    cursor.close()
    db.close()
