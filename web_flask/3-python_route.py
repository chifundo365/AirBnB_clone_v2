#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """ manages the / route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ handles the /hbnb route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ handles the /c/<text> route """
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
def display_python(text):
    """ Handles the /python and /python/<text> route """
    return 'python {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run()
