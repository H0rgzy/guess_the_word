from database import db


# models


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    team = db.Column(db.String(50), unique = True, index= False)

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    country = db.Column(db.String(50), unique = True, index= False)

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    animal = db.Column(db.String(50), unique = True, index= False)