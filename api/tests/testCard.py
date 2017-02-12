from cards import Card
import pytest

class Test_Card():

    def test_constuctor_card_none(self):
        jackOfHearts = Card()
        assert 'card' not in jackOfHearts.__dict__.keys()
        assert 'suit' not in jackOfHearts.__dict__.keys() 
    
    def test_constuctor_suit_none(self):
        aceOfHearts = Card('AH')
        assert aceOfHearts.card == 'A'
        assert aceOfHearts.suit == 'H'

    def test_constuctor_card2_suit(self):
        aceOfClubs = Card('AC','S')
        assert aceOfClubs.card == 'A'
        assert aceOfClubs.suit == 'C'

    def test_constuctor_card_suit(self):
        aceOfSpades = Card('A','S')
        assert aceOfSpades.card == 'A'
        assert aceOfSpades.suit == 'S'

    def test_constuctor_bad_input(self):
        aceOfSpades = Card('Ace','Spades')
        assert 'card' not in aceOfSpades.__dict__.keys()
        assert 'suit' not in aceOfSpades.__dict__.keys() 

