from flask import Flask, render_template, url_for, flash, redirect
from covidapp import app, db, bcrypt
from covidapp.forms import LoginForm
from covidapp.models import Autoritaire
from flask_login import login_user, current_user, logout_user, login_required

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
    form = LoginForm()
    if form.validate_on_submit():
        if form.autoritaire.data == True:
            autoritaire = Autoritaire.query.filter_by(email=form.email.data).first()
            if autoritaire and bcrypt.check_password_hash(autoritaire.password, form.password.data):
                login_user(autoritaire)
                return redirect(url_for('home'))
        else:
            medecin = Medecin.query.filter_by(email=form.email.data).first()
            if medecin and bcrypt.check_password_hash(medecin.password, form.password.data):
                login_user(medecin)
                return redirect(url_for('home'))

    return render_template("login.html", title="Connecter", form=form)

@app.route("/deconnecter")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/compte")
@login_required
def account():
    return render_template("account.html", title="Compte")

