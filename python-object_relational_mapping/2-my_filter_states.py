#!/usr/bin/python3
''' Lists all states from the database hbtn_0e_0_usa.'''

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

# Créer un objet curseur pour exécuter des requêtes SQL
    cur = db.cursor()

# Exécuter la requête  sélectionne les lignes de la table "states" avec le nom
# spécifié
    state_name_searched = sys.argv[4]
    query = "SELECT * FROM `states` WHERE `name` = %s ORDER BY id ASC;"

    cur.execute(query, (state_name_searched,))

# Récupérer toutes les lignes  de la requête dans une liste et les afficher
    states = cur.fetchall()
    for state in states:
        print(state)

# Fermer le curseur et la connexion à la base de données
    cur.close()
    db.close()
