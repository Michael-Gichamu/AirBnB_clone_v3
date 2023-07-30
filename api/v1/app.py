#!/usr/bin/python3
"""Flask Application"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

default_host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
default_port = os.environ.get('HBNB_API_PORT', '5000')


@app.teardown_appcontext
def db_teardown(exception):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """Main function"""
    app.run(host=default_host, port=default_port, threaded=True)
