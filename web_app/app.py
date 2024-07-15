#!/usr/bin/python3
"""Entry point of the web application"""

# from models import storage
from flask import Flask, render_template, request
from flask_jwt_extended import verify_jwt_in_request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from os import getenv
from web_app.views import web_views


app = Flask(__name__)
app.register_blueprint(web_views)

# Set up JWT configuration
app.secret_key = 'aidalley_jwt_secret_key'

jwt = JWTManager(app)  # Initialize JWTManager with the app


# @app.teardown_appcontext
# def teardown_db(exception):
#     """Closes current SQLAlchemy session after each request"""
#     storage.close()


@app.before_request
def load_jwt_tokens():
    """Load JWT tokens from cookies before each request"""
    access_token = request.cookies.get('access_token')
    if access_token:
        request.headers = dict(request.headers)  # Convert headers to a mutable dict
        request.headers['Authorization'] = f'Bearer {access_token}'


@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 error"""
    return render_template('404.html'), 404


if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
    host = getenv('AIDBLEY_WEB_HOST', '0.0.0.0')
    port = int(getenv('AIDBLEY_WEB_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
