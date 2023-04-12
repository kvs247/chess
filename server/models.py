from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-_password_hash', '-friendships', 'friend_ids', '-white_games', '-black_games', 'game_ids',)

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String())
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True)
    profile_image = db.Column(db.String())
    date_joined = db.Column(db.DateTime(), server_default=db.func.now())

    friendships = db.relationship('Friendship', foreign_keys='Friendship.user_id', backref='user')

    @property
    def friend_ids(self):
        friends_duplicated = [f.friend_id for f in self.friendships]
        return list(set(friends_duplicated))

    white_games = db.relationship('Game', foreign_keys='Game.white_user_id', backref='white_user')
    black_games = db.relationship('Game', foreign_keys='Game.black_user_id', backref='black_user')

    @property
    def game_ids(self):
        return [g.id for g in self.white_games + self.black_games]

    _password_hash = db.Column(db.String())

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    
class Friendship(db.Model, SerializerMixin):
    __tablename__ = 'friendships'

    serialize_rules = ('-user', '-friend')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

    serialize_rules = ('-white_user', '-black_user')

    id = db.Column(db.Integer, primary_key=True)
    white_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    black_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pgn = db.Column(db.String())
    fen = db.Column(db.String())

class Challenge(db.Model, SerializerMixin):
    __tablename__ = 'challenges'

    serialize_rules = ('-challenger', '-challengee')

    id = db.Column(db.Integer, primary_key=True)
    challenger_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    challengee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String())
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))