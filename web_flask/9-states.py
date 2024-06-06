#!/usr/bin/python3
"""
Start a Flask web application on host add 127.0.0.1 port 50000
handles two routes /states and /states/<id>
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """ displays all the states in storage """
    states = list(storage.all(State))
    return render_template("9-states.html", states=states, page="states")

@app.route("/states/<id>", strict_slashes=False)
def states_with_id(id):
    """ Displays a state of the given id and its cities """
    states = list(storage.all(State))
    matched = None
    for state in states:
        if state.id == id:
            matched = state
            break
    return render_template("9-states.html", state=matched)


