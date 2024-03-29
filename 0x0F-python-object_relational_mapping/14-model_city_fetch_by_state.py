#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sqlalchemy as db
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for state, city in session.query(State, City)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
