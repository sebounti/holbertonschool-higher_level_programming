#!/usr/bin/python3
'''
Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], database=argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY `name` = '{}'".format(argv[4]))

    states = cur.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)

    cur.close()
    db.close()
