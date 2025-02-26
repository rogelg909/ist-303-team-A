# test_quiz.py - Unit tests for CodeQuest

import unittest
from app import app

class CodeQuestTest(unittest.TestCase):
    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_addition(self):
        assert 2 + 2 == 4  # Placeholder test

if __name__ == "__main__":
    unittest.main()

