#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)


    # Initialize engine
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    state_name_searched = sys.argv[4]

    query = session.query(State).filter_by(name=state_name_searched).first()

    # Conditions
    if query:
        print("{:d}".format(query.id))
    else:
        print("Not found")

    # Close session
    session.close()
