#!/usr/bin/python3
"""Starts a Flask web app.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displaying string 'Hello HBNB!'.
    /hbnb: Displaying string 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying string 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
