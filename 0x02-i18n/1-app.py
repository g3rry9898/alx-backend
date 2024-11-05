#!/usr/bin/env python3
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Use Config class as config for your Flask app
app.config.from_object(Config)

if __name__ == "__main__":
    app.run(debug=True)

