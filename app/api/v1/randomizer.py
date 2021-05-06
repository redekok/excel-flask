"""
API namespace that returns a random number within a given range
"""
from flask_restx import Namespace, Resource, fields
from random import randint

api = Namespace('randomizer', description='Generate random number within given range [min, max]')

## Setup the parser for the request parameters
parser = api.parser()

parser.add_argument(
    'min',
    type=int,
    required=True,
    help='Minimum of the range (integer)',
    location='form')

parser.add_argument(
    'max',
    type=int,
    required=True,
    help='Maximum of the range (integer)',
    location='form')

# parser.add_argument(
#     'environment', type=str, required=True,
#     help='The environment of the Energy Transition Model ("beta" or "pro")',
#     location='form'
# )

## Controller
@api.route('/')
@api.doc()
class Randomizer(Resource):
    """
    Return random number within given range
    """
    @api.expect(parser)
    def post(self):
        """
        Create random number within the range based on the given minimum and
        maximum integers
        """
        args = parser.parse_args()

        min = args['min']
        max = args['max']

        random = randint(min, max)

        return {
            'random': random
        }
