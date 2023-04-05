from app import app
from models import db, User

with app.app_context():

    User.query.delete()

    # Create users
    print('Creating users...')
    users = [
        User(
            full_name='Kyle Schneider',
            username='Kye_Schnei',
            email='kyles@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/woody.jpg?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Topher Ludlow',
            username='topherLud',
            email='topher@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/topher.jpg?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Bobby Fischer',
            username='BobbyIsTheBest',
            email='bobby@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/bobby.jpg?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Garry Kasparov',
            username='KasparovKingKiller',
            email='garry@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/garry.jpg?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Hans Niemann',
            username='I am not a cheater',
            email='hans@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/hans.jpg?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Hikaru Nakamura',
            username='Hikaru',
            email='hikaru@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/hikaru.png?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Levy Rozman',
            username='Gotham Chess',
            email='levy@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/levy.png?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Magnus Carlsen',
            username='DrDrunkenstein',
            email='magnus@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/magnus.jpg?raw=true',
            password_hash='password'
        ),
        User(
            full_name='Ian Nepomniachtchi',
            username='NepoTheNimbleNight',
            email='ian@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/ian.jpeg?raw=true',
            password_hash='password'
        )

    ]

    print('Seeding database...')
    db.session.add_all(users)
    db.session.commit()

    print('Done')