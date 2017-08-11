#!/usr/bin/python3

"""
list cities that is passed in through argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    query2 = """SELECT cities.name
    FROM cities WHERE cities.state_id
    IN (SELECT states.id
    FROM states WHERE states.name = %s)"""
    cur = db.cursor()
    cur.execute(query2, (sys.argv[4],))
    result = cur.fetchall()

    array = []
    for i in result:
        i = str(i)
        array.append(i)

    for j in range(len(array)):
        array[j] = array[j].replace('(', '')
        array[j] = array[j].replace(')', '')
        array[j] = array[j].replace('\'', '')
        array[j] = array[j].replace(',', '')

    string = ', '.join(array)
    print(string)
    cur.close()
    db.close()
