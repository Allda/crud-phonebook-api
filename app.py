from flask import Flask, redirect, request, render_template
from cs50 import SQL

app = Flask(__name__)

# cs50 library was used to make a connection to db
db = SQL("sqlite:///phonebook.db")

@app.route("/")
def index():
    '''Index page. User can use "Contacts" button
    to be redirected to /contacts page and see the database.'''
    return render_template("index.html")

@app.route("/contacts")
def read_all():
    '''After calling this route user will see
    the phonebook database.'''
    contacts = db.execute("SELECT * FROM phonebook")
    return render_template("contacts.html", contacts=contacts)

