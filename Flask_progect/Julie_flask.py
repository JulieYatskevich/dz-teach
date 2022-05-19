from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Games %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/catalog')
def catalog():
    game_catalog = Games.query.order_by(Games.price).all()
    return render_template("catalog.html",game_catalog=game_catalog)


@app.route('/catalog/<int:id>')
def about_game(id):
    one_game = Games.query.get(id)
    return render_template("about_game.html",one_game=one_game)    



@app.route('/catalog/<int:id>/del')
def catalog_delete(id):
    one_game = Games.query.get_or_404(id)
    try:
        db.session.delete(one_game)
        db.session.commit()
        return redirect('/catalog')
    except:
        return "При удалении произошла ошибка"




@app.route('/add_game', methods=['POST','GET'])
def add_game():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        year = request.form['year']

        game = Games(name=name, price=price, year=year) 

        try:
            db.session.add(game) 
            db.session.commit()
            return redirect('/catalog')
        except:
            return "При добавлении статьи произошла ошибка"

    else:
        return render_template("add_game.html") 



if __name__ == "__main__":
    app.run(debug=True)