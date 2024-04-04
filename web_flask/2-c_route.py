#!/usr/bin/python3
"""Starting a Flask web app.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displaying string 'Hello HBNB!'.
    /hbnb: Displaying string 'HBNB'.
    /c/<text>: showing 'C' followed by the val of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Shows string 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Shows 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displaying 'C' followed by the val of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
