from datetime import datetime
from covidapp import db, login_manager
from flask_login import UserMixin

# Add constraints cchecking later when having time

@login_manager.user_loader
def user_loader(user_id):
    if Autoritaire:
        return Autoritaire.query.get(int(user_id))

    return Medecin.query.get(int(user_id))

class Autoritaire(db.Model, UserMixin):
    __tablename__ = "autoritaires"

    id = db.Column(db.Integer, primary_key=True)
    nom_complet = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"<Autoritaire('{self.nom_complet}', '{self.email}')>"

class Zone(db.Model):
    __tablename__ = "zones"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(40), nullable=False)
    wilaya = db.Column(db.String(40), nullable=False)
    # population = db.Column(db.Integer, primary_key=True, nullable=False)
    centre = db.relationship('CentreVaccination', backref='zone', uselist=False)

    def __repr__(self):
        return f"<Zone('{self.id}', '{self.nom}', '{self.wilaya}')>"

class CentreVaccination(db.Model):
    __tablename__ = "centres"

    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id'), nullable=False)

    meds = db.relationship('Medecin', backref='centrevac')

    def __repr__(self):
        return f"<CentreVaccination('{self.id}', '{self.zone_id}')>"
 
class Medecin(db.Model, UserMixin):
    __tablename__ = "medecins"

    id = db.Column(db.Integer, primary_key=True)
    nom_complet = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    centre_id = db.Column(db.Integer, db.ForeignKey('centres.id'), nullable=False)

    def __repr__(self):
        return f"<Medecin('{self.nom_complet}', '{self.email}', '{self.centre_id}')>"

class Variant(db.Model):
    __tablename__ = "variants"

    id = db.Column(db.Integer, primary_key=True)
    whoLabel = db.Column(db.String(15), nullable=False, unique=True)
    firstIdentified = db.Column(db.String(30), nullable=False)

    patients = db.relationship('ProfilPatient', backref='varnt', lazy='dynamic')

    def __repr__(self):
        return f"<Variant('{self.id}', '{self.whoLabel}', '{self.firstIdentified}')>"

class UtilisateurMobile(db.Model):
    __tablename__ = "utilisateurs"

    id = db.Column(db.Integer, primary_key=True)
    nom_complet = db.Column(db.String(60), nullable=False)
    patients = db.relationship('ProfilPatient', backref='utilisateurMobile')
    
    def __repr__(self):
        return f"<UtilisateurMobile('{self.id}', '{self.nom_complet}')>"
 

class ProfilPatient(db.Model):
    __tablename__ = "patients"

    code = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    nom_complet = db.Column(db.String(60), nullable=False)
    degreVulnerabilite = db.Column(db.Integer, nullable=False) 

    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'), nullable=False)

    variant_id = db.Column(db.Integer, db.ForeignKey('variants.id'))
    degreSeverite = db.Column(db.Integer)

    demande = db.relationship('DemandeVaccination', backref='patient', uselist=False)

    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id'), nullable=False)

    def __repr__(self):
        return f"<Profil patient('{self.code}', '{self.nom_complet}', '{self.age}', '{self.sex}')"
 

class Vaccin(db.Model):
    __tablename__ = "vaccins"

    id = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(50), nullable=False)
    paysFabrication = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Vaccin('{self.id}', '{self.designation}', '{self.paysFabrication}')>"

  
class DemandeVaccination(db.Model):
    __tablename__ = "demandes"

    id = db.Column(db.Integer, primary_key=True)
    code_patient = db.Column(db.Integer, db.ForeignKey("patients.code"), nullable=False)

    vaccination = db.relationship('Vaccination', backref='demande', uselist=False)
    convocation = db.relationship('Convocation', backref='convoc', uselist=False)

    def __repr__(self):
        return f"<DemandeVaccination('{self.id}', '{self.code_patient}')>"


class Vaccination(db.Model):
    __tablename__ = "vaccinations"

    id = db.Column(db.Integer, primary_key=True)
    demande_id = db.Column(db.Integer, db.ForeignKey("demandes.id"), nullable=False, unique=True) 
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Vaccination('{self.id}', '{self.date}')>"

class Convocation(db.Model):
    __tablename__ = "convocations"

    id = db.Column(db.Integer, primary_key=True)
    demande_id = db.Column(db.Integer, db.ForeignKey('demandes.id'), nullable=False)

    def __repr__(self):
        return f"<Convocation('{self.id}', '{self.demande_id}')>"