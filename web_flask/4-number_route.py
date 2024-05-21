#!/usr/bin/python3
""" This is a basic Flask web_server"""
from flask import Flask
app = Flask(__name__)

# Enable debugger --line 13 (for development only)
# Enforce strict slashes
app.url_map.strict_slashes = False


@app.route("/number/<int:n>")
def display_number(n):
    """
        Converts n to a number , else returns 404 error.
        <int:n> ensures to convert parameter, to an integer, if possible
    """
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
