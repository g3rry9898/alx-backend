#!/usr/bin/env python3
"""
This module sets up a basic Flask app with Babel for internationalization and user login emulation.
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel, _
from typing import Optional, Dict, Any

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Use Config class as config for your Flask app
app.config.from_object(Config)

def get_user() -> Optional[Dict[str, Any]]:
    """
    Get user dictionary or None if the ID cannot be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request() -> None:
    """
    Execute before all other functions to find a user if any and set it as a global on flask.g.user.
    """
    g.user = get_user()

@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determine the best match for supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

