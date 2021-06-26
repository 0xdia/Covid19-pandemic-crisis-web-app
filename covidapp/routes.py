from flask import Flask, render_template, url_for, flash, redirect
from covidapp import app
from covidapp.forms import RegistrationForm, LoginFrom
from covidapp.models import Autoritaire

@app.route("/")
@app.route("/acceuil")
def home():
    return render_template("home.html")

@app.route("/connexion", methods=["GET", "POST"]):
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)
