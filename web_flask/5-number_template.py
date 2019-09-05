#!/usr/bin/python3
# Script that starts a Flask web application
# Web application listening on 0.0.0.0, port 5000
# Route '/' displays "Hello HBNB!"
# Route '/hbnb' displays "HBNB"
# Route '/c/<text>' displays value of the text variable (replace '_' with ' ')
# Route '/python/(<text>)' displays 'Python' followed by route above ^
# ("is cool" default val) of ^
# Route '/number/<n>' displays 'n is a number' only if "n" is an int
# Route '/number_template/<n>' displays html page only if above ^

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


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_a_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
