#!/usr/bin/python3
# Script that starts a Flask web application
# Web application listening on 0.0.0.0, port 5000
# Route '/' displays "Hello HBNB!"
# Route '/hbnb' displays "HBNB"

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
