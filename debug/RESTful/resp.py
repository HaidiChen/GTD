from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Todo1(Resource):
    def get(self):
        # default 200 OK
        return {'task': 'Hello World'}

class Todo2(Resource):
    def get(self):
        # set the response code to 201
        return {'task': 'Hello, World'}, 201

class Todo3(Resource):
    def get(self):
        # set the response code to 201 and return
        # custom headers
        return {'task': 'hello, world'}, 201, {'Etag': 'some-opaque-string' }

class HelloWorld(Resource):
    def get(self):
        return {'return': 'Hello, World'}

api.add_resource(Todo1, '/t1')
api.add_resource(Todo2, '/t2', endpoint='todo2')
api.add_resource(Todo3, '/t3', endpoint='todo3')
api.add_resource(HelloWorld, '/', '/hello/')

if __name__ == "__main__":
    app.run(debug=True)
