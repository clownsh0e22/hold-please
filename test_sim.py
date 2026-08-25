import unittest
from app import app

class TestIVRSimulation(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_voice_endpoint_initial(self):
        response = self.app.post("/voice", data={})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Response", response.data)

    def test_voice_endpoint_billing(self):
        response = self.app.post("/voice", data={"SpeechResult": "billing"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"response", response.data.lower())

if __name__ == "__main__":
    unittest.main()
