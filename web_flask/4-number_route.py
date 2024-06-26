#!/usr/bin/python3
"""Startnggs a Flask web app.

App listens on 0.0.0.0, port 5000.
Routes:
    /: Displaying 'Hello HBNB!'.
    /hbnb: Displayingg 'HBNB'.
    /c/<text>: Displaying 'C' followed by the <text> value.
    /python/(<text>): Displays 'Python' followed by the <text> value.
    /number/<n>: Displays 'n is a no. only if <n> is an int.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying string 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying char 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displaying 'C' followed by the <text> value.

    Replacing underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displaying 'Python' followed by the <text> value.

    Replacing any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displaying 'n is a no. only if n is an int."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
