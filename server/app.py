# import os
# from dotenv import load_dotenv
# load_dotenv()

import random
from flask import request, session, make_response, jsonify, abort, render_template
from flask_restful import Resource

from models import User, Game, Friendship, Challenge
from config import app, db, api
from chess.main import Chess
from chess.pgn_to_fen import pgn_to_fen, pgn_to_fen_store, pgn_to_dict, update_fen
from chess import util
from chess.new_pgn import new_pgn

@app.route('/play')
@app.route('/play/<int:id>')
@app.route('/profile')
@app.route('/profile/<int:id>')
@app.route('/about')
@app.route('/login')
@app.route('/signup')
@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

class Users(Resource):
    def get(self):
        return make_response(
            [u.to_dict() for u in User.query.all()],
            200
        )
api.add_resource(Users, '/users')

class UserById(Resource):
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            return make_response(user.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
        
    def patch(self, id):
        data = request.json
        color_hex = data['boardColor']
        user = User.query.filter_by(id=id).first()
        user.board_color = color_hex
        db.session.add(user)
        db.session.commit()
        return make_response(user.to_dict(), 200)
api.add_resource(UserById, '/users/<int:id>')

class Friendships(Resource):
    def get(self):
        return make_response(
            [f.to_dict() for f in Friendship.query.all()],
            200
        )
    
    def post(self):
        data = request.json
        db.session.add_all(
            [Friendship(user_id=data[0], friend_id=data[1]),
            Friendship(user_id=data[1], friend_id=data[0])]
        )
        db.session.commit()

    def delete(self):
        data = request.json
        db.session.delete(
            Friendship.query.filter_by(user_id=data[0], friend_id=data[1]).first()
        )
        db.session.delete(
            Friendship.query.filter_by(user_id=data[1], friend_id=data[0]).first()
        )
        db.session.commit()
api.add_resource(Friendships, '/friendships')

class Games(Resource):
    def get(self):
        return make_response(
            [g.to_dict() for g in Game.query.all()],
            200
        )
    
    def post(self):
        data = request.json
        random.shuffle(data)
        pgn = new_pgn(data[0]['username'], data[1]['username'])
        game = Game(
            white_user_id=data[0]['id'],
            black_user_id=data[1]['id'],
            pgn = pgn,
            fen = pgn_to_fen(pgn)
        )
        db.session.add(game)
        db.session.commit()
        return(make_response(game.to_dict(), 201))
        
api.add_resource(Games, '/games')

class GameById(Resource):
    def get(self, id):
        try:
            game = Game.query.filter_by(id=id).first()
            response = game.to_dict().copy()
            response['fen_list'] = pgn_to_fen_store(game.pgn)
            return make_response(response, 200)
        except Exception as e:
            return make_response({'error': str(e)}, 404)
    
    def patch(self, id):
        request_data = request.json
        # print(request_data)
        from_index = request_data['fromIndex']
        to_index = request_data['toIndex']


        game = Game.query.filter_by(id=id).first()
        fen = game.fen
        pgn = game.pgn
        fen_dict = util.fen_to_dict(fen)
        pgn_dict = pgn_to_dict(pgn)
        chess = Chess(fen)

        # print(pgn_to_fen_store(game.pgn))

        if pgn_dict['result'] != '*':
            print('game ended')
            return make_response(jsonify(game.fen), 200)

        # user ended game
        if from_index == -1:
            # resignation
            if request_data['resign']:
                username = request_data['resign']
                if username == pgn_dict['white_username']:
                    game.pgn = game.pgn.replace('*', '0-1')
                else:
                    game.pgn = game.pgn.replace('*', '1-0')
                db.session.add(game)
                db.session.commit()
                return make_response(jsonify(game.fen), 200)

        move = chess.move(from_index, to_index)
        # print('move', move)
        
        if move:
            # stalemate
            stalemate = False
            if '$' in move:
                move = move.replace('$', '')
                stalemate = True

            # promotion
            promotion_type = None
            if '=' in move:
                promotion_type = move[-1]
                fen_dict = util.fen_to_dict(game.fen)
                active_color = fen_dict['active_color']
                if active_color == 'b':
                    promotion_type = promotion_type.lower()
            
            # update pgn and fen
            move_number = ''
            newline = ''
            if fen_dict['active_color'] == 'w':
                move_number = str(fen_dict['fullmove_number']) + '. '
                if len(pgn.splitlines()[-1]) > 60:
                    newline = '\n'
            new_pgn = pgn[:-1] + newline + move_number + move + ' ' + pgn[-1]
            if stalemate:
                new_pgn = new_pgn.replace('*', '1/2-1/2')

            # checkmate
            if '#' in move:
                win_string = '1-0' if fen_dict['active_color'] == 'w' else '0-1'
                new_pgn = new_pgn.replace('*', win_string)
                
            game.pgn = new_pgn
            game.fen = update_fen(game.fen, from_index, to_index, promotion_type)
            fen_dict = util.fen_to_dict(game.fen)

            # 50 move draw
            if fen_dict['halfmove_clock'] == 100:
                print('draw')
                game.pgn = game.pgn.replace('*', '1/2-1/2')

            # threefold repetition
            fen_list  = pgn_to_fen_store(game.pgn)
            fen_list = list(map(lambda x: x.split(' ')[0], fen_list))
            game_fen_string = game.fen.split(' ')[0]
            if game_fen_string in fen_list[:-1]:
                # print('repeated once')
                temp_fen_list = fen_list[:-1]
                temp_fen_list.remove(game_fen_string)
                if game_fen_string in temp_fen_list:
                    # print('repeated twice')
                    game.pgn = game.pgn.replace('*', '1/2-1/2')

            # insufficient material
            fen_list = util.piece_placement_to_list(fen_dict['piece_placement'])

            db.session.add(game)
            db.session.commit()

        print(pgn_to_fen_store(game.pgn))
        
        return make_response(jsonify(pgn_to_fen_store(game.pgn)), 200)

api.add_resource(GameById, '/games/<int:id>')

class Challenges(Resource):
    def get(self):
        return make_response(
            [c.to_dict() for c in Challenge.query.all()],
            201
        )
    
    def post(self):
        data = request.json
        db.session.add(
            Challenge(
                challenger_id=data['challengerId'], 
                challengee_id=data['challengeeId'],
                status='pending'
            )
        )
        db.session.commit()
        return make_response({}, 201)
api.add_resource(Challenges, '/challenges')

class ChallengeById(Resource):
    def get(self, id):
        try:
            challenge = Challenge.query.filter_by(id=id).first()
            return make_response(challenge.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 404)
        
    def delete(self, id):
        challenge = Challenge.query.filter_by(id=id).first()
        db.session.delete(challenge)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(ChallengeById, '/challenges/<int:id>')

class Login(Resource):
    def post(self):
        data = request.json
        try:
            user = User.query.filter_by(email=data['email']).first()
            if user.authenticate(data['password']):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
            else:
                abort(404, 'Incorrect email or password')
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(Login, '/login')

class SignUp(Resource):
    def post(self):
        data = request.json
        try:
            user = User(
                full_name=data['fullName'],
                username=data['username'],
                email=data['email'],
                profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/default.png?raw=true',
                password_hash=data['password']
            )
            db.session.add(user)
            db.session.commit()
            return make_response(user.to_dict(), 201)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(SignUp, '/signup')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({}, 204)
api.add_resource(Logout, '/logout')

class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            return make_response(user.to_dict(), 200)
        except Exception as e:
            return make_response({'error': str(e)}, 400)
api.add_resource(AuthorizedSession, '/authorized-session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)