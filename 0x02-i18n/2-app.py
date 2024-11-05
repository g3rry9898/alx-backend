#!/usr/bin/env python3
"""
This module sets up a basic Flask app with Babel for internationalization.
"""

from flask import Flask, request
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Use Config class as config for your Flask app
app.config.from_object(Config)

@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determine the best match for supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(debug=True)

