import datetime
from faker import Faker

fake = Faker()
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2015, 12, 31)

user_dicts = [
    {
        'full_name': 'Kyle Schneider',
        'username': 'Kye_Schnei',
        'email': 'kyle@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/woody.jpg?raw=true',
        'date_joined': datetime.date(2020, 11, 23),
        'password_hash': 'password'
    },
    {
        'full_name': 'Topher Ludlow',
        'username': 'topherLud',
        'email': 'topher@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/topher.jpg?raw=true',
        'date_joined': datetime.date(2020, 11, 10),
        'password_hash': 'password'
    },
    {
        'full_name': 'Magnus Carlsen',
        'username': 'DrDrunkenstein',
        'email': 'magnus@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/magnus.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Bobby Fischer',
        'username': 'BobbyBlitzBoy',
        'email': 'bobby@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/bobby.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Garry Kasparov',
        'username': 'KasparovKingKiller',
        'email': 'garry@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/garry.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Hans Niemann',
        'username': 'Hans Solo',
        'email': 'hand@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/hans.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Hikaru Nakamura',
        'username': 'Hikaru',
        'email': 'hikaru@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/hikaru.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Levy Rozman',
        'username': 'Gotham Chess',
        'email': 'levy@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/levy.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Fabiano Caruana',
        'username': 'FabulousFabiano',
        'email': 'fabiano@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/fabiano.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Maxime Vachier-Lagrave',
        'username': 'MVLchess',
        'email': 'maxime@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/maxime.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Wesley So',
        'username': 'SoSneaky',
        'email': 'wesley@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/wesley.png?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Viswanathan Anand',
        'username': 'Vishy',
        'email': 'vishy@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/viswanathan.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Levon Aronian',
        'username': 'The Levonator',
        'email': 'levon@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/levon.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Anish Giri',
        'username': 'GiriGiri',
        'email': 'anish@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/anish.jpg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    },
    {
        'full_name': 'Ian Nepomniachtchi',
        'username': 'Nepo',
        'email': 'ian@fake.com',
        'profile_image': 'https://github.com/kschneider0/chess/blob/main/server/assets/ian.jpeg?raw=true',
        'date_joined': fake.date_between(start_date=start_date, end_date=end_date),
        'password_hash': 'password'
    }
]

friendship_pairs = [
    (1, 10), (1, 13), (1, 3), (1, 14), (1, 8),  
    (2, 4), (2, 12), (2, 11), (2, 6), (2, 15),  
    (3, 1), (3, 9), (3, 12), (3, 7), (3, 5),  
    (4, 2), (4, 10), (4, 9), (4, 7), (4, 13),  
    (5, 8), (5, 14), (5, 11), (5, 12), (5, 6),  
    (6, 2), (6, 7), (6, 13), (6, 8), (6, 15),  
    (7, 3), (7, 4), (7, 12), (7, 6), (7, 15),  
    (8, 1), (8, 5), (8, 10), (8, 6), (8, 14),  
    (9, 4), (9, 3), (9, 15), (9, 13), (9, 10),  
    (10, 1), (10, 9), (10, 4), (10, 14), (10, 11),  
    (11, 2), (11, 5), (11, 13), (11, 10), (11, 15),  
    (12, 2), (12, 5), (12, 7), (12, 3), (12, 9),  
    (13, 1), (13, 4), (13, 6), (13, 11), (13, 9),  
    (14, 1), (14, 10), (14, 8), (14, 5), (14, 15),  
    (15, 2), (15, 6), (15, 7), (15, 11), (15, 9)
]