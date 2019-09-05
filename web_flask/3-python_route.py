#!/usr/bin/python3
# Script that starts a Flask web application
# Web application listening on 0.0.0.0, port 5000
# Route '/' displays "Hello HBNB!"
# Route '/hbnb' displays "HBNB"
# Route '/c/<text>' displays value of the text variable (replace '_' with ' ')
# Route '/python/(<text>)' displays 'Python' followed by route above ^
# ("is cool" default val) of ^

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_(text):
    return ("C " + text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_cool(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
