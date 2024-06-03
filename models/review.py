#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base, String, ForeignKey, Column
from models import storage_t


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    if storage_t == "db":
        __tablename__ = "Reviews"
        text = Column(String(1024), nullable=False)
<<<<<<< HEAD
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False) 
=======
        place_id = Column(String(60), ForeignKey("places.id") nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
>>>>>>> e6adfaec4c6d80a6d6711dc2b07ed9d9779d6836
    else:
        place_id = ""
        user_id = ""
        text = ""
