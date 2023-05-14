import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

CORS(app)
bcrypt = Bcrypt(app)
# os.environ.get('DATABASE_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # development
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://chess_db_30un_user:gZ7L2y8CaxEsV9fedv9JTPgDxlr55HZ9@dpg-cgk4m7seoogkndh25el0-a.oregon-postgres.render.com/chess_db_30un'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b'\x7f\\Q\x15\xc9\xc9\xfc\x1e`\x96s\xb8\xbc\xd8'

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)