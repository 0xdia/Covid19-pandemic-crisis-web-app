from covidapp import db

class Autoritaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100). unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Autoritaire('{self.username}', '{self.email}')"

