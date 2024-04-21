#!/usr/bin/python3
""" Starts a Flask Web Application for HBNB """
from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message when /hbnb is called """
    return 'Hello from HBNB!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
