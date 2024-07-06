#!/usr/bin/python3
"""Entry point of the web application"""

# from models import storage
from flask import Flask, render_template
from flask_cors import CORS
from os import getenv
from web_app.views import web_views


app = Flask(__name__)
app.register_blueprint(web_views)


# @app.teardown_appcontext
# def teardown_db(exception):
#     """Closes current SQLAlchemy session after each request"""
#     storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 error"""
    return render_template('404.html'), 404


if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
    host = getenv('AIDBLEY_WEB_HOST', '0.0.0.0')
    port = int(getenv('AIDBLEY_WEB_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
