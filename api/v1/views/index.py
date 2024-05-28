#!/usr/bin/python3
'''
Creating a Flask application plus app_views
'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    """

    """
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/status')
def get_status():
    """

    """
    stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User'),
    }

    return jsonify(stats)
