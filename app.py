from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testing'
app.config['MONGO_DBNAME'] = 'BASE'
app.config['MONGO_URI'] = 'mongodb+srv://admin:1234@cluster0.cbutodz.mongodb.net/BASE?retryWrites=true&w=majority'

mongo = PyMongo(app)
alumnos_collection = mongo.db.alumnos


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
    if request.method == 'POST':
        alumnos = mongo.db.alumnos  # Cambiado de users a alumnos
        existing_alumno = alumnos.find_one({'username': request.form['username']})

        if existing_alumno:
            flash(request.form['username'] + ' username already exists')
            return redirect(url_for('signup'))

        hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        alumnos.insert_one({'username': request.form['username'], 'password': hashed, 'email': request.form['email']})
        return redirect(url_for('signin'))

    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        alumnos = mongo.db.alumnos  # Cambiado de users a alumnos
        signin_alumno = alumnos.find_one({'username': request.form['username']})

        if signin_alumno:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), signin_alumno['password']) == signin_alumno[
                'password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        flash('Username/password is incorrect')
        return render_template('signin.html')

    return render_template('signin.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
    app.run()
