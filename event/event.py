import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


master_part = db.Table('master_part',
    db.Column('part_id', db.Integer, db.ForeignKey('participants.id')),
    db.Column('master_id', db.Integer, db.ForeignKey('masterklass.id'))
)

class Masterklass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Masterklass {self.name}>'
    

class Participants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    following = db.relationship('Masterklass', secondary=master_part, backref='followers')


    def __repr__(self):
        return f'<Participants {self.first_name}>'


@app.route('/')
def index():
        return render_template ("index.html")


if __name__ == "__main__":
    app.run(debug=True)
