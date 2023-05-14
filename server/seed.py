import glob

from app import app
from models import db, User, Friendship, Game, Challenge
from chess.pgn_to_fen import pgn_to_dict, pgn_to_fen

from data.users import user_dicts
from data.friendships import friendship_pairs

pgn_files = glob.glob('./data/PGNs/*.pgn')
pgn_strs = []
for f in pgn_files:
    with open(f) as f:
        pgn_strs.append(f.read())

with app.app_context():

    db.create_all()

    Challenge.query.delete()
    Game.query.delete()
    Friendship.query.delete()
    User.query.delete()

    # Create users
    print('Creating users...')
    def make_user(user_dict):
        return User(
            id=user_dict['id'],
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
    users.sort(key=lambda u: u.date_joined)
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
    # starting position
    game = Game(
        id=0,
        white_user_id=0,
        black_user_id=0,
        pgn = '[Date \"1980.06.18\"]\n[Result \"*\"]\n[White \"Kye_Schnei\"]\n[Black \"topherLud\"]\n\n*',
        fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    )
    games.append(game)
    i = 1
    for pgn in pgn_strs:
        pgn_dict = pgn_to_dict(pgn)
        # print(pgn_dict['move_list'])

        white_username = pgn_dict['white_username']
        white_user_id = User.query.filter_by(username=white_username).first().id
        
        black_username = pgn_dict['black_username']
        black_user_id = User.query.filter_by(username=black_username).first().id

        game = Game(
            id=i,
            white_user_id=white_user_id,
            black_user_id=black_user_id,
            pgn=pgn
        )
        try:
            game.fen = pgn_to_fen(pgn)
        except Exception as e:
            game.fen = str(e)
        games.append(game)

        i += 1

    games.sort(key=lambda g: pgn_to_dict(g.pgn)['date'])
    db.session.add_all(games)

    db.session.commit()

    print('Done')