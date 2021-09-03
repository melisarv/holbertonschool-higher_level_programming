#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa"""

import sqlalchemy as db
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    result = session.query(State).order_by(State.id).first()
    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
    session.close()
