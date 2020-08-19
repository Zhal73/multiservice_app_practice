from unittest.mock import patch
  
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
class TestMovieApp(TestBase):
    #check if the animal is in ["Dog","Cat","Lion","Cow","Donkey"]
    #line 10-15 routes.py
    def test_getanimal(self):
        response = self.client.get(url_for('get_animal'))
        check = False
        for item in ["Dog","Cat","Lion","Cow","Donkey"]:
            if bytes.decode(response.data) == item:
                check = True
        self.assertTrue(check)
    
    def test_getnoise(self):
        with patch('requests.get') as g:
                g.return_value.text = "Dog"
                response = self.client.post(url_for('get_noise'),data=g.return_value.text)
                self.assertIn(b'Woof', response.data)

