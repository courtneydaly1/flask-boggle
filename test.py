from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
 # TODO -- write tests for every view function / feature!

def setUp(self):
    """before all tests"""
    self.client = app.test_client()
    app.config['TESTING'] = True

    def test_homepage(self):
        """make sure data is displayed as well as board"""
        with self.client:
            res = self.client.get('/')
            self.assertIn("board", session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('num_plays'))
            self.assertIn(b'<p>High Score:', res.data)
            self.assertIn(b"Score:", res.data)
            self.assertIn(b"Seconds Left:", res.data)

def test_valid_word(self):
    """test if word is valid by modifying board"""
    with self.client as client:
        with client.session_transaction() as sess:
            sess['board'] = [["C", "A", "T", "T", "T"], 
                            ["C", "A", "T", "T", "T"], 
                            ["C", "A", "T", "T", "T"], 
                            ["C", "A", "T", "T", "T"], 
                            ["C", "A", "T", "T", "T"]]
            res =self.client.get("/check-word?word=cat")
            self.assertEqual(res.json['result'], "ok")

def test_invalid_word(self):
    """test if word is on the board"""
    self.client.get('/')
    res =self.client.get('/check-word?word=maniac')
    self.assertEqual(res.json['result'], "not-on-board")

def test_if_word(self):
    """test to see is a valid word in dict"""
    self.client.get("/")
    res= self.client.get('/check-word?word=hikittycat')
    self.assertEqual(res.json["result", 'not-word'])