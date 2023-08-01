#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # Créer le moteur de base de données
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Initialiser la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # requête pour récup tous les enregistrements de la table State triés parid
    query = session.query(State).order_by(State.id).all()

    # Afficher le résultat de la requête
    for record in query:
        print("{}: {}".format(record.id, record.name))

    # Fermer la session
    session.close()
