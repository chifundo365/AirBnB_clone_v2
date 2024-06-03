#!/usr/bin/python3
""" Amenity  Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, String, Column
from models import storage_t


if storage_t =="db":
    from models.place import place_amenities


class Amenity(BaseModel):
    if storage_t == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities  = relationship("Place", secondary=place_amenities,
                                        back_populates="amenities")
    else:
        name = ""

