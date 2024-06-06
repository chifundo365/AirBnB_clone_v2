#!/usr/bin/python3
"""
Start a Flask web appilcation [127.0.0.1:5000]
"""
from flask import Flask, render_template
from models import storage, storage_t
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ Fetches all the states from the storage engines """
    states_dict = storage.all(State)
    return render_template("7-states_list.html", states=states_dict)


@app.teardown_appcontext
def remove_sqlalchemy_session(exc):
    storage.close()


if __name__ == "__main__" and storage_t == "db":
    app.run()
