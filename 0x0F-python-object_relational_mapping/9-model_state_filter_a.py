#!/usr/bin/python3
"""lists all State objects that contain the letter a"""

import sqlalchemy as db
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    for result in session.query(State).order_by(State.id).all():
        if 'a' in result.name:
            print("{}: {}".format(result.id, result.name))

    session.close()
