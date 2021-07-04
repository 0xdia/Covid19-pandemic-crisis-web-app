from covidapp import app, db
from covidapp.models import *
from sqlalchemy import desc
import datetime

def next_time(string):
    lst = string.split()
    hour, minute = lst[-1].split(":")

    if int(minute) + 10 < 60:
        minute = str(int(minute)+10)
    else:
        minute = str(int(minute)+10-60)
        if len(minute) == 1:
            minute = "0" + minute

        hour = str(int(hour)+1)
        if len(hour) == 1:
            hour = "0" + hour

    rep = ""
    for i in range(len(lst)-1):
        rep += lst[i] + " "

    return rep + hour + ":" + minute

def date(string):
    lst = string.split()

    days = {
        "Sat": "Samedi",
        "Sun": "Dimanche",
        "Mon": "Lundi",
        "Tue": "Mardi",
        "Wed": "Mercredi",
        "The": "Jeudi",
        "Fri": "Vendredi"
    }

    months = {
        "Jun": "Jan", "Feb": "Fev", "Mar": "Mar", "Apr": "Avr", "May": "Mai", "Jun": "Juin",
        "Jul": "Juil", "Aug": "Aou", "Sep": "Sep", "Oct": "Oct", "Nov": "Nov", "Dec": "Dec"
    }

    lst[3] = lst[3][:5]

    rep = days[lst[0]] + " " + lst[2] + " " + months[lst[1]] + " " + lst[-1] + ", " + lst[-2]
    return rep

#results = ProfilPatient.query.filter(ProfilPatient.age > 70).all()

dairas = Zone.query.all()

zones = {}

for daira in dairas:
    zones[daira.id] = []

# results = db.session.query(ProfilPatient).filter(ProfilPatient.age > 70).all()

patients = ProfilPatient.query.order_by(desc(ProfilPatient.age)).all()

for patient in patients:
    zones[patient.zone_id].append([patient.code, patient.nom_complet])

for key, value in zones.items():
    x = datetime.datetime.now()
    d = date(x.strftime("%c"))

    for patient in value:
        patient.extend([f"centre de vaccination {Zone.query.filter_by(id=key).first().nom}", d])
        d = next_time(d)

print(dairas)
# for key, value in zones.items():
#     print(key)
#     print(value)

