#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”"""

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

    city = City(name='San Francisco')
    state = State(name='California', cities=[city])
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
