from datetime import datetime
from covidapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(user_id):
    if Autoritaire:
        return Autoritaire.query.get(int(user_id))

    return Medecin.query.get(int(user_id))

class Autoritaire(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Autoritaire('{self.nom}', '{self.prenom}', '{self.email}')"

class Medecin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20), nullable=False)
    prenom = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Medecin('{self.nom}', '{self.prenom}', '{self.email}')"

class ProfilPatient(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    degreVulnerabilite = db.Column(db.Integer, nullable=False) 
    utilisateurMobileID = db.Column(db.Integer, db.ForeignKey('UtilisateurMobile.id'), nullable=False)
    zoneID = db.Column(db.Integer, db.ForeignKey('Zone.id'), nullable=False)

    def __repr__(self):
        return f"Profil patient('{self.code}')"

class Variant(db.Model):
    #nomScientifique = db.Column(db.String(50), nullable=False)
    whoLebel = db.Column(db.String(15), primary_key=True)

    def __repr__(self):
        return f"Variant('{self.whoLebel}')"

class ProfilPatient_Variant(db.Model):
    degreSeverite = db.Column(db.Integer, nullable=False)
    profilCode = db.Column(db.Integer, db.ForeignKey('ProfilPatient.code'), primary_key=True)
    variantID = db.Column(db.String, db.ForeignKey('Variant.id'), primary_key=True)

    def __repr__(self):
        return f"ProfilCode: {self.profilCode}, VariantID: {self.variantID}, Degre severite: {self.degreSeverite}"

class UtilisateurMobile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return f"UtilisateurMobile('{self.id}'"
  
class Vaccin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(50), nullable=False)
    paysFabrication = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Vaccin('{self.designation}'"

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    population = db.Column(db.Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return f"Zone: {self.id}"

'''
class CentreVaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
class DemandeVaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

class Vaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)

class Convocation(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
'''