#!/usr/bin/python3
"""Starts a Flask web app.

The app listens on 0.0.0.0, port 5000.
Routes:
    /: Displaying str 'Hello HBNB!'.
    /hbnb: Displaying 'HBNB'.
    /c/<text>: Displaying 'C' followed by the <text> value.
    /python/(<text>): Displays 'Python' followed by the <text> value.
    /number/<n>: Displays 'n is a number' only if <n> is an int.
    /number_template/<n>: Displaying an HTML page only if <n> is an int.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying str 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displaying 'C' followed by the <text> value

    Replacing any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displaying 'Python' followed by the <text> value

    Replacing underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displaying 'n is a number' only if <n> is an int."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an int."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
