#!/usr/bin/python3
"""
list all states from database hbtn_0e_0_usa
with names that start with capiatl 'N'
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    query = """SELECT * FROM states WHERE name LIKE BINARY 'N%'
    ORDER BY states.id ASC;"""
    cur = db.cursor()
    cur.execute(query)
    result = cur.fetchall()

    for i in result:
        print(i)
    cur.close()
    db.close()
