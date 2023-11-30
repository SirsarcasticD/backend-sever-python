import unittest
import requests


class TestPing(unittest.TestCase):

    def test_ping(self):

        response = requests.get("http://127.0.0.1:8000/ping/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{"ping": "ok"}')
