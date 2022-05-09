import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Obrabotka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Obrabotka {self.first_name}>'


class Osnovi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name1 = db.Column(db.String, nullable=False)
    last_name1 = db.Column(db.String, nullable=False)
    phone1 = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Osnovi {self.first_name1}>'


@app.route('/')
def index():
        return render_template ("index.html")


@app.route('/obrabotka-foto',  methods=['GET', 'POST'])
def obr_foto():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']

        obrabotka = Obrabotka(first_name=first_name, last_name=last_name, phone=phone)

        try:
            db.session.add(obrabotka)
            db.session.commit()
            return redirect ('/')
        except:
            return "При добавлении произошла ошибка"
    return render_template ("obrabotka.html")


@app.route('/osnovi-foto',  methods=['GET', 'POST'])
def osnovi():
    if request.method == "POST":
        first_name1 = request.form['first_name1']
        last_name1 = request.form['last_name1']
        phone1 = request.form['phone1']
        
        osnovi = Osnovi(first_name1=first_name1, last_name1=last_name1, phone1=phone1)
        
        try:
            db.session.add(osnovi)
            db.session.commit()
            return redirect ('/')
        except:
            return "При добавлении произошла ошибка"

    return render_template ("osnovi.html")


if __name__ == "__main__":
    app.run(debug=True)
