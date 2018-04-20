from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
import mysql.connector
import os

app = Flask(__name__)
db = mysql.connector.connect(user='root', password='pw', host='localhost', database='codenames')


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome back!"


@app.route('/login', methods=['POST'])
def login():
    query = ("SELECT password from users where username = %s")
    username = request.form['username']
    cursor = db.cursor()
    cursor.execute(query, username)

    if request.form['password'] == cursor[0]['password']:
        session['logged_in'] == True
    else:
        flash('Bad credentials')
    return home()
