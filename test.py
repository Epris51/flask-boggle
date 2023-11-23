from app import app
from unittest import TestCase

class FlaskTests(TestCase):

    def setUp(self):
        """Set up before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_new_game(self):
        """Test starting a new game."""
        with self.client as client:
            response = client.get('/new-game')
            self.assertIn('board', response.json)
            self.assertIsInstance(response.json['board'], list)
            self.assertEqual(len(response.json['board']), 5)  # Assuming a 5x5 board

    def test_valid_guess(self):
        """Test making a valid guess."""
        with self.client as client:
            response = client.get('/new-game')
            board = response.json['board']
            guess_response = client.post('/guess', json={'word': 'TEST', 'board': board})
            self.assertIn(guess_response.json['result'], ['ok', 'not-on-board', 'not-word'])

    def test_invalid_guess(self):
        """Test making an invalid guess."""
        with self.client as client:
            response = client.get('/new-game')
            board = response.json['board']
            guess_response = client.post('/guess', json={'word': 'INVALID', 'board': board})
            self.assertEqual(guess_response.json['result'], 'not-word')

    # Add more tests as needed for other functionalities
