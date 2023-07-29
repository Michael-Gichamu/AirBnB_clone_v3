#!/usr/bin/python3
"""Index route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns status of API"""
    return jsonify({"status": "OK"})
