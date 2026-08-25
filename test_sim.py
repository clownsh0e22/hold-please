import unittest
from app import app

class TestTwilioWebhooks(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_voice_webhook_navigation(self):
        response = self.client.post('/voice', data={'CallSid': 'CA12345', 'SpeechResult': 'I need help with my bill'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<Response>', response.data)
        self.assertIn(b'<Play digits=', response.data)

    def test_voice_webhook_hold_detection(self):
        response = self.client.post('/voice', data={'CallSid': 'CA12345', 'SpeechResult': 'Please hold for the next representative'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<Pause length="5" />', response.data)

if __name__ == '__main__':
    unittest.main()
