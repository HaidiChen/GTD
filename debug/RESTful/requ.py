from flask import Flask 
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to change for this Resource')


class Price(Resource):
    def post(self):
        args = parser.parse_args()
        rate = args['rate']
        if rate:
            rate = str(rate * 100)
            return {'price': rate}
        return {'price': 'nothing'}

api.add_resource(Price, '/price')

if __name__ == "__main__":
    app.run(debug=True)
