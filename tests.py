import crud
import os
import unittest
from flask import session
from server import app
from unittest import TestCase
from model import Child, Location, User, Tracking, connect_to_db, db


class ChildTestCase(TestCase):
    
    def test_index(self):
        self.assertEqual(crud.get_child_by_id(1), "<Child name=Katele Caldera missing_age=17 >")


class FlaskIntegrationTestCase(TestCase):
    """Testing flask server"""

    def test_index(self):
        client = app.test_client()
        result = client.get('/')
        self.assertIn(b"<div id='map'></div>", result.data)
    

class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session"""

    def setUp(self):
        """Stuff to do before every test"""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = "dev"
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['email'] = "user@user.com"

    def test_tracking_page(self):
        """Check tracking page."""

        result = self.client.get("/tracking-page")
        self.assertIn(b'<div class="state-item">', result.data)



if __name__ == "__main__":
    #if called like a script, run our tests

    os.system('dropdb testdb')
    os.system('createdb testdb')

    unittest.main(verbosity=2)

 