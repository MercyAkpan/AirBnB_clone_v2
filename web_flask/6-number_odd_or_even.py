#!/usr/bin/python3
""" This is a basic Flask web_server"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

# Enable debugger --line 13 (for development only)
# Enforce strict slashes
app.url_map.strict_slashes = False


@app.route("/number_odd_or_even/<int:n>")
def display_number_template(n):
    """
        Converts n to a number , else returns 404 error.
        <int:n> ensures to convert parameter, to an integer, if possible
        render_template simply needs a file.. 
        that should be in the default: "templates" folder.
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
