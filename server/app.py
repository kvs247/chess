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

class Login(Resource):
    def post(self):
        data = request.json
        print(data)
        try:
            user = User.query.filter_by(email=data['email']).first()
            if user.authenticate(data['password']):
                session['user_id'] = user.id
                return make_response(
                    user.to_dict(),
                    200
                )
        except Exception as e:
            return make_response(
                {'error': str(e)},
                400
            )
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(port=5555, debug=True)