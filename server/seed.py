import glob
import random
import re

from app import app
from models import db, User, Friendship, Game
from pgn_fen_handler import pgn_to_dict

from data.users import user_dicts
from data.friendships import friendship_pairs

pgn_files = glob.glob('./data/PGNs/*.pgn')
pgn_strs = []
for f in pgn_files:
    with open(f) as f:
        pgn_strs.append(f.read())

with app.app_context():

    User.query.delete()
    Friendship.query.delete()
    Game.query.delete()

    # Create users
    print('Creating users...')
    def make_user(user_dict):
        return User(
            full_name=user_dict['full_name'],
            username=user_dict['username'],
            email=user_dict['email'],
            profile_image=user_dict['profile_image'],
            date_joined=user_dict['date_joined'],
            password_hash=user_dict['password_hash']
        )
    users = []
    for user in user_dicts:
        users.append(make_user(user))
    random.shuffle(users)
    db.session.add_all(users)

    # Create friendships
    print('Creating friendships...')
    friendships = []
    for (user_id, friend_id) in friendship_pairs:
        friendships.append(Friendship(user_id=user_id, friend_id=friend_id))
    db.session.add_all(friendships)

    # Create games
    print('Creating games...')
    games = []
    for pgn in pgn_strs:
        pgn_dict = pgn_to_dict(pgn)

        white_username = pgn_dict['white_username']
        white_user_id = User.query.filter_by(username=white_username).first().id
        
        black_username = pgn_dict['black_username']
        black_user_id = User.query.filter_by(username=black_username).first().id

        game = Game(
            white_user_id=white_user_id,
            black_user_id=black_user_id,
            pgn=pgn
        )
        games.append(game)
    games.sort(key=lambda g: pgn_to_dict(g.pgn)['date'])
    db.session.add_all(games)

    db.session.commit()

    print('Done')