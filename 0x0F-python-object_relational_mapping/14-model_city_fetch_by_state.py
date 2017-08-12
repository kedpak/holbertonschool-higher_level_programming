#!/usr/bin/python3
"""
print all city objects from database
"""

import sqlalchemy
from model_city import City, Base
from model_state import State, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    for cities in session.query(State, City).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(
            cities.State.name, cities.City.id, cities.City.name))
