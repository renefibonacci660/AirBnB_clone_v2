#!/usr/bin/python3
# Script that starts a Flask web application
# Web application listening on 0.0.0.0, port 5000 (by default)
# Route '/' displays "Hello HBNB!"

from flask import Flask

if __name__ == "__main__":
    app.run(host="0.0.0.0")

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB")
