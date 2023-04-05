from flask import request, session, make_response, jsonify, abort
from flask_restful import Resource

from models import User
from config import app, db, api

class Users(Resource):
    def get(self):
        return make_response(
            [u.to_dict() for u in User.query.all()],
            200
        )
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(port=5555, debug=True)