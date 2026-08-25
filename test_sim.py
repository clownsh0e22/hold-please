import unittest
from app import app

class TestTwilioWebhooks(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_voice_webhook(self):
        response = self.client.post('/voice', data={'SpeechResult': 'I need help with my bill'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<Response>', response.data)
        self.assertIn(b'<Play digits=', response.data)

if __name__ == '__main__':
    unittest.main()
