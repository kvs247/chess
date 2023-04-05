from flask import request, session, make_response, jsonify, abort
from flask_restful import Resource

from config import app, db, api

class Test(Resource):
    def get(self):
        return make_response({'hello': 'world'}, 200)
api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(port=5555, debug=True)