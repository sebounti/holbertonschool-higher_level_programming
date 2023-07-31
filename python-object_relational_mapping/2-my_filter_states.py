#!/usr/bin/python3
''' Lists all states from the database hbtn_0e_0_usa.'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()

    # Utiliser un paramètre de liaison pour la valeur de la requête SQL
    state_name_searched = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    cur.execute(query, (state_name_searched,))

    states = cur.fetchall()

    for state in states:
        print(state)
