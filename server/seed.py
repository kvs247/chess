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
            username='',
            email='bobby@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/bobby.jpg?raw=true',
        ),
        User(
            full_name='Garry Kasparov',
            username='',
            email='garry@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/garry.jpg?raw=true',
        ),
        User(
            full_name='Hans Niemann',
            username='',
            email='hans@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/hans.jpg?raw=true',
        ),
        User(
            full_name='Hikaru Nakamura',
            username='',
            email='hikaru@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/hikaru.png?raw=true',
        ),
        User(
            full_name='Levy Rozman',
            username='',
            email='levy@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/levy.png?raw=true',
        ),
        User(
            full_name='Magnus Carlsen',
            username='DrDrunkenstein',
            email='magnus@fake.com',
            profile_image='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Magnus_Carlsen_2013.jpg/220px-Magnus_Carlsen_2013.jpg',
        ),
        User(
            full_name='Ian Nepomniachtchi',
            username='',
            email='ian@fake.com',
            profile_image='https://github.com/kschneider0/chess/blob/main/server/assets/garry.jpg?raw=true',
        )

    ]

    print('Seeding database...')
    db.session.add_all(users)
    db.session.commit()

    print('Done')