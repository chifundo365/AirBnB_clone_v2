#!/usr/bin/python3
"""
Start a Flask application on ip address 0.0.0.0 and port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """"Loads all the states and states"""
    states = list(storage.all(State).values())
    amenities =list( storage.all(Amenity).values())
    return render_template("10-hbnb_filters.py", states=states, amenities=amenities)

@app.teardown_app_context
def close_sqlalchemy_session(excp):
    """Removes the current sqlalchemy session"""
    storage.close()
