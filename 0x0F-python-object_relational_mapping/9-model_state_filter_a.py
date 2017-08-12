#!/usr/bin/python3
"""
list all objects that contain the letter 'a'
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

    Session = sessionmaker(engine)
    session = Session()

    state_obj = session.query(State)

    for i in range(len(state_obj.all())):
        if "a" in state_obj[i].name:
            print("{}: {}".format(state_obj[i].id, state_obj[i].name))
    session.commit()
    session.close()
