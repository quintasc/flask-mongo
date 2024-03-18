from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testing'
app.config['MONGO_DBNAME'] = 'BASE'
app.config['MONGO_URI'] = '...'

mongo = PyMongo(app)
alumnos_collection = mongo.db.users


@app.route("/")
@app.route("/main")
def main():

    return render_template('index.html')


@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])

    return render_template('index.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
   

@app.route('/signin', methods=['GET', 'POST'])
def signin():
   

@app.route('/logout')
def logout():
  

if __name__ == "__main__":
    app.run(debug=True)
    app.run()
