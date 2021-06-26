from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from covidapp.forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'af9rt9zr2h4tzhz4892pok'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from covidapp import routes

