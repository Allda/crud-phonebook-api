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

@app.route("/add")
def add_contact():
    '''Function is used to create a new entry in database.
    User will provide URL arguments to create a new entry.'''
    name = request.args.get("name")
    surname = request.args.get("surname")
    phone = request.args.get("phone")
    address = request.args.get("address")
    db.execute('''INSERT INTO phonebook 
        (name, surname, phone, address) VALUES(?, ?, ?, ?)''', name, surname, phone, address)
    return redirect("/contacts")

