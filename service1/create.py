# import the SQLAlchemy instance
from application import db

from application.models import animal_noise

db.drop_all()

db.create_all()


