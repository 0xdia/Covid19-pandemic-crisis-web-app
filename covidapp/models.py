from datetime import datetime
from covidapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(autoritaire_id):
    return Autoritaire.query.get(int(autoritaire_id))

class Autoritaire(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Autoritaire('{self.nom}', '{self.prenom}', '{self.email}')"

class Medecin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Medecin('{self.nom}', '{self.prenom}', '{self.email}')"
