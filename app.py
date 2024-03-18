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
   # Inserta tu código aquí
    pass


@app.route('/index')
def index():
    # Inserta tu código aquí
    pass


@app.route("/signup", methods=['POST', 'GET'])
def signup():
   # Inserta tu código aquí
    pass

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    # Inserta tu código aquí
    pass
   

@app.route('/logout')
def logout():
  # Inserta tu código aquí
    pass

if __name__ == "__main__":
    app.run(debug=True)
    app.run()
