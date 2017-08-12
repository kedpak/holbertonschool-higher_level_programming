#!/usr/bin/python3
"""
prints the first State object
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import State, Base

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    """  Base.metadata.create_all(engine) """

    Session = sessionmaker(engine)
    session = Session()
    state_name = session.query(State.name, State.id).order_by(State.id).all()
    print("{}: {}".format(state_name[0][1], state_name[0][0]))
    session.commit()
    session.close()
