#!/usr/bin/python3
"""sts all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id")

    rows = c.fetchall()
    for i in rows:
        print(i)
    c.close()
    db.close()
