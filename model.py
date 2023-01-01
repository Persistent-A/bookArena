from enum import unique
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

#Using db.Model, setting database field columns containing required data.
class Books(db.Model):
    title = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    author = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return {'title': {self.title}, 'author':{self.author}, 'genre':{self.genre}, 'description':{self.description}, 'price':{self.price}}