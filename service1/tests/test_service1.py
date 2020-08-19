from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        return app

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
##### TESTS IMPLEMENTATION  ########


