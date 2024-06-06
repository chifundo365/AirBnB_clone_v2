#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_t
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, Column, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_t == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ''

        @property
        def cities(self):
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

    def __init__(self, *args, **kwargs):
        """ init method for the State class """
        super().__init__(*args, **kwargs)
