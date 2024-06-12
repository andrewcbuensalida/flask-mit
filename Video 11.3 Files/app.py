import re
from flask import Flask, request, render_template, session
from flask import redirect
from functools import wraps
import os
app = Flask(__name__)
app.secret_key = "secretkey"
app.config["UPLOADED_PHOTOS_DEST"] = "static"

books = [
    {
        "author": "Hernando de Soto",
        "country": "Peru",
        "language": "English",
        "pages": 209,
        "title": "The Mystery of Capital",
        "year": 1970,
    },
    {
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "language": "Danish",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836,
    },
    {
        "author": "Dante Alighieri",
        "country": "Italy",
        "language": "Italian",
        "pages": 928,
        "title": "The Divine Comedy",
        "year": 1315,
    },
]

users = [{"username": "testuser", "password": "testuser"}]


def checkUser(username, password):
    for user in users:
        if username in user["username"] and password in user["password"]:
            return True
    return False


@app.route("/", methods=["GET"])
def firstRoute():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username  = request.form["username"]
        password  = request.form["password"]
        if checkUser(username, password):
            session["username"] = username
            return render_template("index.html", username = session["username"])
        else:
            return render_template("register.html")

    elif request.method == "GET":
        return render_template("register.html")



@app.route("/logout")
def logout():
     # remove the username from the session if it is there
    session.pop("username", None)
    return "Logged Out of Books"


@app.route("/", methods=["GET"])
def getBooks():
        return render_template('books.html', books=books,  username=session["username"])
#add decorator for books


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
