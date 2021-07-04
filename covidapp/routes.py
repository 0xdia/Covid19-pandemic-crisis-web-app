from flask import Flask, render_template, url_for, flash, redirect
from covidapp import app, db, bcrypt
from covidapp.forms import LoginForm
from covidapp.models import *
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc
import datetime
from docx import Document


@app.route("/")
@app.route("/accueil")
def home():
    return render_template("home.html", title="Accueil")

@app.route("/inscrire")
def register():
    form = RegisterForm()
    return render_template("register.html", title="Inscrire", form=form)

@app.route("/connecter", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        if form.autoritaire.data == True:
            autoritaire = Autoritaire.query.filter_by(email=form.email.data).first()
            if autoritaire and bcrypt.check_password_hash(autoritaire.password, form.password.data):
                login_user(autoritaire)
                return redirect(url_for('home_autoritaire'))
        else:
            medecin = Medecin.query.filter_by(email=form.email.data).first()
            if medecin and bcrypt.check_password_hash(medecin.password, form.password.data):
                login_user(medecin)
                return redirect(url_for('home_medecin'))

    return render_template("login.html", title="Connecter", form=form)

@app.route("/home/autoritaire")
@login_required
def home_autoritaire():
    return render_template("home_autoritaire.html")

@app.route("/home/medecin")
@login_required
def home_medecin():
    return render_template("home_medecin.html")

@app.route("/deconnecter")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/compte")
@login_required
def account():
    return render_template("account.html", title="Compte")

@app.route("/planning")
@login_required
def planning():
    def create_convocation(nom_complet, centre, date):
        document = Document('/home/dhiaa/arena/github/Covid19-pandemic-crisis-web-app/covidapp/static/Convocation de vaccination.docx')

        i = 1
        for paragraph in document.paragraphs:
            # print(f"{i}: {paragraph.text}")
        
            if i == 5:
                paragraph.insert_paragraph_before(nom_complet)

            if i == 7:
                paragraph.insert_paragraph_before(f"{centre}, {date}")

            i += 1

        document.save(f'/home/dhiaa/arena/github/Covid19-pandemic-crisis-web-app/covidapp/convocations/Convocation de vaccination_{nom_complet}.docx')


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

      
    return render_template("planning.html", title="Planning de vaccination", zones=zones, dairas=dairas)
