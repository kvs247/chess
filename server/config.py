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
@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template('index.html')

CORS(app)
bcrypt = Bcrypt(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # development
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b'\x7f\\Q\x15\xc9\xc9\xfc\x1e`\x96s\xb8\xbc\xd8'

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)