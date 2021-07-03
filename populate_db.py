import csv
from covidapp import db, app
from covidapp.models import *

print("[*] Dropping all tables")
db.drop_all()

print("[*] Creating all tables")
db.create_all()

print("[*] populating the db")

# populating vaccins table
with open('covidapp/data/vaccins.csv') as vaccins:
    vaccins_reader = csv.reader(vaccins, delimiter=',')

    i = 0
    for row in vaccins_reader:
        if i != 0:
            v = Vaccin(id=row[0], designation=row[1], paysFabrication=row[2])                    
            db.session.add(v)

        i += 1

# populating variants table
with open('covidapp/data/variants.csv') as variants:
    variants_reader = csv.reader(variants, delimiter=',')

    i = 0
    for row in variants_reader:
        if i != 0:
            v = Variant(whoLabel=row[0], firstIdentified=row[1])                    
            db.session.add(v)

        i += 1

# populating variants table
with open('covidapp/data/variants.csv') as variants:
    variants_reader = csv.reader(variants, delimiter=',')

    i = 0
    for row in variants_reader:
        if i != 0:
            vr = Variant(id=row[0], whoLabel=row[1], firstIdentified=row[2])                    
            if Variant.query.filter_by(id=row[0]).count() < 1:
                db.session.add(vr)

        i += 1

# populating zones (dairas) table
with open('covidapp/data/dairas.csv') as zones:
    zones_reader = csv.reader(zones, delimiter=',')

    i = 0
    for row in zones_reader:
        if i != 0:
            z = Zone(id=row[0], nom=row[1], wilaya=row[2])                    
            db.session.add(z)

        i += 1

# populating centres_vaccination table
with open('covidapp/data/centres_vaccination.csv') as centres:
    centres_reader = csv.reader(centres, delimiter=',')

    i = 0
    for row in centres_reader:
        if i != 0:
            c = CentreVaccination(id=row[0], zone_id=row[1])                    
            db.session.add(c)

        i += 1

# populating utilisateurs mobile table
with open('covidapp/data/utilisateurs.csv') as utilisateurs:
    utilisateurs_reader = csv.reader(utilisateurs, delimiter=',')

    i = 0
    for row in utilisateurs_reader:
        if i != 0:
            u = UtilisateurMobile(id=row[0], nom_complet=row[1])                    
            db.session.add(u)

        i += 1

# populating medecins table
with open('covidapp/data/medecins.csv') as medecins:
    medecins_reader = csv.reader(medecins, delimiter=',')

    i = 0
    for row in medecins_reader:
        if i != 0:
            if Medecin.query.filter_by(email=row[2]).count() < 1:
                m = Medecin(id=row[0], nom_complet=row[1], email=row[2], password=row[3], centre_id=row[4])                    
                db.session.add(m)

        i += 1

# populating patients table
with open('covidapp/data/patients.csv') as patients:
    patients_reader = csv.reader(patients, delimiter=',')

    i = 0
    for row in patients_reader:
        if i != 0:
            if ProfilPatient.query.filter_by(code=row[0]).count() < 1:
                p = ProfilPatient(
                                    code=row[0], age=row[1], sex=row[2], 
                                    nom_complet=row[3], 
                                    degreVulnerabilite=row[4], utilisateur_id=row[5],
                                    variant_id=row[6], degreSeverite=row[7],
                                    zone_id=row[8]
                                )                    

                db.session.add(p)

        i += 1

# populating demandes table
with open('covidapp/data/demandes_vaccination.csv') as demandes:
    demandes_reader = csv.reader(demandes, delimiter=',')

    i = 0
    for row in demandes_reader:
        if i != 0:
            d = DemandeVaccination(id=row[0], code_patient=row[1])                    
            db.session.add(d)

        i += 1

with open('covidapp/data/autorites.csv') as autorites:
    autorites_reader = csv.reader(autorites, delimiter=',')

    i = 0
    for row in autorites_reader:
        if i != 0:
            if Autoritaire.query.filter_by(email=row[2]).count() < 1:
                m = Autoritaire(id=row[0], nom_complet=row[1], email=row[2], password=row[3])                    
                db.session.add(m)

        i += 1


db.session.commit()

#print("[*] Querying all vaccins")
#print(Vaccin.query.all())

# This needs to be fixed
#print("[*] Querying all variants")
#print(Variant.query.all())

#print("[*] Querying all zones (dairas)")
#print(Zone.query.all())

#print("[*] Querying all centers")
#print(CentreVaccination.query.all())

#print("[*] Querying all mobile users")
#print(UtilisateurMobile.query.all())

#print("[*] Querying all medecins")
#print(Medecin.query.all())

#print("[*] Querying all patients")
#print(ProfilPatient.query.all())

#print("[*] Querying all demandes")
#print(DemandeVaccination.query.all())

#print("[*] Querying all autorites")
#print(Autoritaire.query.all())

