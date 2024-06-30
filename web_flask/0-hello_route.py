#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def home_page():
    """ Flask View that handles the airbnb-onepage route"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(port=5000)
