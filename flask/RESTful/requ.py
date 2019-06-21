from flask import Flask 
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('rate', type=int, help='Rate to change for this Resource')

# argument is required
parser.add_argument('name', required=True,
        action='append', help="Name cannot be blank!")
parser.add_argument('foo', type=int, required=True, choices=(1, 2),
        help='Bad choice: {error_msg}')

# change the name of argument when it is parsed
parser.add_argument('color', dest='public_color')

class Price(Resource):
    def post(self):
        args = parser.parse_args()
        rate = args['rate']
        names = args['name']
        pc = args['public_color']
        if rate:
            rate = str(rate * 100)
            return {'price': rate, 'names': names}
        return {'price': 'nothing', 'names': names, 'color': pc}

api.add_resource(Price, '/price')

if __name__ == "__main__":
    app.run(debug=True)
