# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request
import requests
# import the app object from the ./application/__init__.py
from application import app

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/generate_animal',methods=['GET','POST'])
def generate_animal():
    animal = requests.get('service2:5001/get_animal')
    noise = requests.post('service2:5001/get_noise',data=animal.text)
    
    return render_template('generate_animal.html',title='Generate Animal Page',data1=animal.text,data2=noise.text)
