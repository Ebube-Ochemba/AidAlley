#!/usr/bin/python3
"""Entry point of the API"""

from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
# from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


# @app.teardown_appcontext
# def teardown_db(exception):
#     """Closes current SQLAlchemy session after each request"""
#     storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
    host = getenv('AIDBLEY_API_HOST', '0.0.0.0')
    port = int(getenv('AIDBLEY_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
