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
    # checks if the home page is accessible
    # routes.py line 11
    def test_homepage(self):
        response = self.client.get(url_for('home')) #call the home page
        self.assertEqual(response.status_code, 200) #checks if it is accessible. code : 200

    def test_dog_woof(self):
        with patch('requests.get') as g, patch('requests.post') as p:
            g.return_value.text="Dog"
            p.return_value.text="Woof"

            response = self.client.get(url_for('generate_animal'))
            self.assertIn(b'Dog',response.data)

