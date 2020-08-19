# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request
import requests
# import the app object from the ./application/__init__.py
from application import app,db

from application.models import animal_noise

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/generate_animal',methods=['GET','POST'])
def generate_animal():
    animal = requests.get('http://localhost:5001/get_animal')
    noise = requests.post('http://localhost:5001/get_noise',data=animal.text)

    db_data = animal_noise(animal=animal.text,noise=noise.text)
    db.session.add(db_data)
    db.session.commit()
    
    animalRecord=animal_noise.query.all()

    return render_template('generate_animal.html',title='Generate Animal Page',data1=animal.text,data2=noise.text,posts=animalRecord)
