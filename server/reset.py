import glob

from app import app
from models import db, Game, User
from chess.pgn_to_fen import pgn_to_dict, pgn_to_fen

pgn_files = glob.glob('./data/PGNs/*.pgn')
pgn_strs = []
for f in pgn_files:
    with open(f) as f:
        pgn_strs.append(f.read())

with app.app_context():
    
    Game.query.delete()

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
        try:
            game.fen = pgn_to_fen(pgn)
        except Exception as e:
            game.fen = str(e)
        games.append(game)
    games.sort(key=lambda g: pgn_to_dict(g.pgn)['date'])
    db.session.add_all(games)

    db.session.commit()
    