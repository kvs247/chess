import datetime
import random
import re
from faker import Faker

from app import app
from models import db, User, Friendship, Game
from seed_data import user_dicts, friendship_pairs, game_pgns

fake = Faker()
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date.today()

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
    games = []
    for pgn in game_pgns:
        white_username = re.search(r'White "(.*)"', pgn).group(1)
        white_user_id = User.query.filter_by(username=white_username).first().id
        black_username = re.search(r'Black "(.*)"', pgn).group(1)
        black_user_id = User.query.filter_by(username=black_username).first().id
        game = Game(
            white_user_id=white_user_id,
            black_user_id=black_user_id,
            pgn=pgn
        )
        games.append(game)
    db.session.add_all(games)

    db.session.commit()

    print('Done')