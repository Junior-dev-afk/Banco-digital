from app import app
from flask import render_template


@app.route("/")
@app.route("/home")
def index ():
    return render_template("home/home.html")


@app.route("/login")
def login():
    return render_template("login/login.html")

@app.route("/pix")
def pix ():
    return render_template("pix/pix.html")