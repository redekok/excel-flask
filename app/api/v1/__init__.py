'''
Contains the ApiV1 blueprint
'''

from flask import Blueprint
from flask_restx import Api

# Exceptions to be caught
from werkzeug.exceptions import MethodNotAllowed
from app.helpers.exceptions import EnergysystemParseError

# Import namespaces (parts of Api)
from .set_inputs import api as ns_set_inputs

# Setup the blueprint and route for the api
blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    version='1.0',
    title='Excel-Flask test app',
    description='Test app to explore the possibilities for hosting a Flask app \
    based on an Excel model'
)

# Add all the namespaces that we want to be visisble to the api
api.add_namespace(ns_set_inputs)

@api.errorhandler(MethodNotAllowed)
def handle_non_existing_route(error):
    '''Returns a 405'''
    return {'error': f'Allowed methods are {error.valid_methods}'}, 405
