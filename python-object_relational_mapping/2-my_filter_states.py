#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa.
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (argv[4],))

    states = cur.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cur.close()
    db.close()
