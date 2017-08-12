#!/usr/bin/python3
"""
creates a class State which connects to states table
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    links to states table with class attributes id and name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
