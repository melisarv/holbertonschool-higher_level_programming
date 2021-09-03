#!/usr/bin/python3
"""displays the states of hbtn_0e_0_usa where name matches the argument"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE BINARY name = '{:s}'\
    ORDER BY states.id ASC".format(sys.argv[4]))

    rows = c.fetchall()
    for i in rows:
        print(i)
    c.close()
    db.close()
