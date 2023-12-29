import unittest
from main import app

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b"Hello, DevSecOps!")

if __name__ == "__main__":
    unittest.main()
