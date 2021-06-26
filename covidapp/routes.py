from flask import Flask, render_template, url_for, flash, redirect
from covidapp import app
from covidapp.forms import LoginForm
from covidapp.models import Autoritaire

@app.route("/")
@app.route("/accueil")
def home():
    return render_template("home.html")

@app.route("/connecter", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Connecter", form=form)
