#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

# Créer un objet curseur pour exécuter des requêtes SQL
    cur = db.cursor()

# Exécuter la requête SQL pour sélectionner toutes les lignes de la table "states"
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
# Récupérer toutes les lignes résultantes de la requête dans une liste
    states = cur.fetchall()

# Parcourir la liste des états récupérée et afficher chaque état
    for state in states:
        print(state)

    cur.close()
    db.close()
