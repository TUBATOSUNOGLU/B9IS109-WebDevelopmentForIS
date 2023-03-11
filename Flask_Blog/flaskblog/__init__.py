from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='5c2d06c9304afa76925b4b82ab092102'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes
