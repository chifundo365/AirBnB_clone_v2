#!/usr/bin/python3
"""
Implements a DBstorage class to store objects to the Mysql
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


Base = declarative_base()


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Creates the sqlalchemy engine and the session """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                    os.getenv('HBNB_MYSQL_USER'),
                    os.getenv('HBNB_MYSQL_PWD'),
                    os.getenv('HBNB_MYSQL_HOST'),
                    os.getenv('HBNB_MYSQL_DB')
                    ),
                pool_pre_ping=True
                )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.engine)

    def all(self, cls=None):
        """ Query objects from current DB session depending on <cls> """
        obj_dict = {}
        if cls:
            objects = self.session.query(cls).all()
        else:
            objects = self.session.query(User, State, City, Amenity, Place, Review).all()
        if objects:
            for obj in objects:
                key  = '{}.{}'.format(obj.__class__.__name__)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ add the object to the current session"""
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        session_f = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False,
                )
        self.__session = scoped_session(session_f)


