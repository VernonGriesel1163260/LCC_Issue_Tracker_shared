"""
ims_app/__init__.py

This module initializes the Flask application for the LCC Issue Tracker.
It creates and configures the Flask app, sets the secret key, initializes the
database connection and Bcrypt for password hashing, registers the various blueprints,
and sets up error handlers for common HTTP errors.
HTTP error handling is out of scope for this project, so has basic functionality.
"""

from flask import Flask, redirect, url_for, request
from ims_app import connect
from ims_app import db
from flask_bcrypt import Bcrypt
# https://www.clamav.net/ ClamAV can be used to virus scan uploaded files, but is out of the scope of this project.

# create flask app

app = Flask(__name__)
app.secret_key = 'exc8vnu3YMK@qwm-wjw' # Set the "secret key" that our app will use to sign session cookies.
# app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 megabytes. Larger results in a 413 Request Entity Too Large error.

# Set up database connection.
db.init_db(app, connect.dbuser, connect.dbpass, connect.dbhost, connect.dbname)

# Initialise Bcrypt and make it importable
bcrypt = Bcrypt(app)

# Register blueprints
from ims_app.routes import main_bp
from ims_app.views import views_bp
from ims_app.controller import controller_bp
from ims_app.issues import issues_bp
from ims_app.admin import admin_bp

app.register_blueprint(main_bp)
app.register_blueprint(views_bp)
app.register_blueprint(controller_bp)  # TODO auth related routes
app.register_blueprint(issues_bp)
app.register_blueprint(admin_bp)

# define routes for error handling
@app.errorhandler(404)
def not_found_error(error):
    """Redirect to a custom 404 error page when a page is not found."""
    # return redirect(url_for('views_bp.page_not_found'))
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(error):
    """Return a simple message when an internal server error occurs."""
    return "An internal error occurred", 500

@app.errorhandler(413)
def internal_error(error):
    """Return an error message when an uploaded file exceeds the size limit."""
    return "File Size error", 413

@app.errorhandler(405)
def internal_error(error):
    """Return a message when a request method is not allowed for the requested URL."""
    return "Method Not Allowed: The method is not allowed for the requested URL.", 405