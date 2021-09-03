#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""

import sqlalchemy as db
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
