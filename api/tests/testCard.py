from cards import Card
import pytest

class Test_Card():

    def test_constuctor_card_none(self):
        jack_of_hearts = Card()
        assert 'card' not in jack_of_hearts.__dict__.keys()
        assert 'suit' not in jack_of_hearts.__dict__.keys() 
    
    def test_constuctor_suit_none(self):
        ace_of_hearts = Card('AH')
        assert ace_of_hearts.card == 'A'
        assert ace_of_hearts.suit == 'H'

    def test_constuctor_card2_suit(self):
        ace_of_clubs = Card('AC','S')
        assert ace_of_clubs.card == 'A'
        assert ace_of_clubs.suit == 'C'

    def test_constuctor_card_suit(self):
        ace_of_spades = Card('A','S')
        assert ace_of_spades.card == 'A'
        assert ace_of_spades.suit == 'S'

    def test_constuctor_bad_input(self):
        ace_of_spades = Card('Ace','Spades')
        assert 'card' not in ace_of_spades.__dict__.keys()
        assert 'suit' not in ace_of_spades.__dict__.keys() 
