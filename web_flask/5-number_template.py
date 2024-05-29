#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from markupsafe import escape
import logging

app = Flask(__name__)

# Disable Flask's default logging
log = logging.getLogger('werkzeug')
log.disabled = True


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Displays Python and text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n' is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
