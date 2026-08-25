import unittest
from fx_agent import FXAgent

class TestFXAgent(unittest.TestCase):
    def test_get_rate(self):
        agent = FXAgent()
        self.assertEqual(agent.get_rate("USD/EUR"), 1.0)

if __name__ == "__main__":
    unittest.main()
