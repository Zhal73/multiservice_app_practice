#import the db instance
from application import db

#creates a table to save the pair animal-noise
class animal_noise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(100), nullable = False)
    noise = db.Column(db.String(100), nullable = False)
