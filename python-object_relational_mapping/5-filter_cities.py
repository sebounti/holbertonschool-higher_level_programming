#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa.
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", (argv[4], ))

    states = cur.fetchall()
    out = [row[0] for row in states]
    print(', '.join(out))
