from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date, ForeignKey
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    creation_date = db.Column(db.Date, default=func.current_date(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    birth_year = db.Column(db.String(20), unique=False, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    height =  db.Column(db.Integer, unique=False, nullable=False)
    mass =  db.Column(db.Integer, unique=False, nullable=False)
    gender =  db.Column(db.String(80), unique=False, nullable=True)
    hair_color =  db.Column(db.String(80), unique=False, nullable=True)
    skin_color = db.Column(db.String(80), unique=False, nullable=True)
    planet_id = db.Column(db.Integer, ForeignKey('planets.id'))
