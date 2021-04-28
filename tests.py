import model 
import flask
import crud
import server
from unittest import TestCase


class ChildTestCase(TestCase):
    
    def test_index(self):
        self.assertEqual(crud.get_child_by_id(1), "<Child name=Katele Caldera missing_age=17 >")


class FlaskIntegrationTestCase(TestCase):
    """Testing flask server"""

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b"<div id='map'></div>", result.data)
    




if __name__ == "__main__":
    #if called like a script, run our tests
    import unittest

    unittest.main(verbosity=2)

 