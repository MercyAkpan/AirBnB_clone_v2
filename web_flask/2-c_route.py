#!/usr/bin/python3
""" This is a basic Flask web_server"""
from flask import Flask
app = Flask(__name__)

# Enable debugger --line 13 (for development only)
# Enforce strict slashes
app.url_map.strict_slashes = False


@app.route("/c/<text>")
def display_text(text):
    # Replace underscores with spaces
    new_text = text.replace("_", " ")
    # Display "C " followed by the processed text
    return f"C {new_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
