#!/usr/bin/python3
"""
Starts a Flask web apllication [127.0.0.1:5000]
Lists a the states and their respective cities
"""
from flask import Flask, render_template
from models import storage, storage_t
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Fetches all the states and their cities from storage """
    states = list(storage.all(State).values())
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def remove_current_sql_alchemy_session(excp):
    """ Removes the current sqlalchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(port=5000)
