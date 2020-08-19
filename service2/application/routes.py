# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request,Response
import requests
# import the app object from the ./application/__init__.py
from application import app
import random

@app.route('/get_animal',methods=['GET'])
def get_animal():
    animals = ['Dog','Cat','Lion','Cow','Donkey']
    animal = animals[random.randrange(4)]
    return Response(animal,mimetype='text/plain')

@app.route('/get_noise',methods=['GET','POST'])
def get_noise():
    noises={
            "Dog": "Woof",
            "Cat": "Meow",
            "Cow": "Mooooo",
            "Lion": "Roar",
            "Donkey": "Hee-How"
    }
    data_sent = request.data.decode('utf-8')
    noise = noises[data_sent]
    return Response(noise, mimetype='text/plain') 
