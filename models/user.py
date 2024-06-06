#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models import storage_t
from models.base_model import BaseModel, Base, Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if storage_t == 'db':
        __tablename__ = 'users'
        email = Column("email", String(128), nullable=False)
        password = Column("password", String(128), nullable=False)
        first_name = Column("first_name", String(128), nullable=True)
        last_name = Column("last_name", String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """ init method for the User class """
        super().__init__(*args, **kwargs)
