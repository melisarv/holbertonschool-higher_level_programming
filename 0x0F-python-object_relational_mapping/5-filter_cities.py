#!/usr/bin/python3
"""takes a state as an argument and lists all cities of that state"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states ON \
    cities.state_id = states.id WHERE states.name =%s \
    ORDER BY cities.id ASC", (sys.argv[4],))
    rows = c.fetchall()
    print(", ".join([r[0] for r in rows]))
    c.close()
    db.close()
