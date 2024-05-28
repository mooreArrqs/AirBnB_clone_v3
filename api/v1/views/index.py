#!/usr/bin/python3
'''
Creating a Flask application plus app_views
'''
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """

    """
    response = {'status': "OK"}
    return jsonify(response)
