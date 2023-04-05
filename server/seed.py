import datetime
import random
from faker import Faker

from app import app
from models import db, User
from user_data import user_data

fake = Faker()
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date.today()

with app.app_context():

    User.query.delete()

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
    for user in user_data:
        users.append(make_user(user))
    random.shuffle(users)

    # Seed database
    print('Seeding database...')
    db.session.add_all(users)
    db.session.commit()

    print('Done')