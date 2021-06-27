from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from covidapp.forms import LoginForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'af9rt9zr2h4tzhz4892pok'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from covidapp import routes