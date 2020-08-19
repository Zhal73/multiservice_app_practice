# import Flask class from the flask module
from flask import Flask, request

import requests

from flask_sqlalchemy import SQLAlchemy

import os

# create a new instance of Flask and store it in app 
app = Flask(__name__)


# retrieve the environmet variable to connectr to the db
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))

app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))

# create an instance of SQLAlchemy to connect to the db
db = SQLAlchemy(app)


# import the ./application/routes.py file
from application import routes
