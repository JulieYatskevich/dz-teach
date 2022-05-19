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


master_part = db.Table('master_part',
    db.Column('part_id', db.Integer, db.ForeignKey('participants.id'), primary_key=True),
    db.Column('master_id', db.Integer, db.ForeignKey('masterclass.id'), primary_key=True)
)

class Masterclass(db.Model):
    __tablename__ = 'masterclass'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Masterclass {self.name}>'
    



class Participant(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    master_part = db.relationship('Masterclass', lazy='dynamic', secondary=master_part, backref=db.backref('participants', lazy='dynamic'))


    def __repr__(self):
        return f'<Participant {self.first_name}>'



@app.route('/')
@app.route('/home', methods=['GET'])
def index():
        return render_template ("index.html")


@app.route('/masterclasses', methods=['GET'])
def masterclass():
    masterclasses = Masterclass.query.all()
    return render_template('masterclasses.html', masterclasses=masterclasses)


if __name__ == "__main__":
    app.run(debug=True)
