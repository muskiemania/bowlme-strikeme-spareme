from cards import Card
import pytest

class Test_Card():

    def test_get_card_and_suit_card_and_suit_no_suit(self):
        (card, suit) = Card()._Card__get_card_and_suit('JH')
        assert card == 'J'
        assert suit == 'H'

    def test_get_card_and_suit_card_and_suit(self):
        (card, suit) = Card()._Card__get_card_and_suit('A', 'D')
        assert card == 'A'
        assert suit == 'D'

    def test_get_card_and_suit_invalid_card(self):
        (card, suit) = Card()._Card__get_card_and_suit('Ace', 'Spades')
        assert card is None
        assert suit is None

    def test_get_strength(self):
        assert Card('2H')._Card__get_strength() == 2
        assert Card('3H')._Card__get_strength() == 3
        assert Card('4H')._Card__get_strength() == 4
        assert Card('5H')._Card__get_strength() == 5
        assert Card('6H')._Card__get_strength() == 6
        assert Card('7H')._Card__get_strength() == 7
        assert Card('8H')._Card__get_strength() == 8
        assert Card('9H')._Card__get_strength() == 9
        assert Card('TH')._Card__get_strength() == 10
        assert Card('JH')._Card__get_strength() == 11
        assert Card('QH')._Card__get_strength() == 12
        assert Card('KH')._Card__get_strength() == 13
        assert Card('AH')._Card__get_strength() == 14
        
    def test_eq(self):
        first_card = Card('JH')
        second_card = Card('JH')
        assert first_card == second_card

        third_card = Card('4', 'D')
        fourth_card = Card('4D')
        assert third_card == fourth_card
    
    def test_constuctor_suit_none1(self):
        ace_of_hearts = Card('AH')
        assert ace_of_hearts.card == 'A'
        assert ace_of_hearts.suit == 'H'
        assert ace_of_hearts.strength == 14

    def test_constuctor_suit_none2(self):
        three_of_hearts = Card('3H')
        assert three_of_hearts.card == '3'
        assert three_of_hearts.suit == 'H'
        assert three_of_hearts.strength == 3
        
    def test_constuctor_card2_suit(self):
        ace_of_clubs = Card('AC','S')
        assert ace_of_clubs.card == 'A'
        assert ace_of_clubs.suit == 'C'
        assert ace_of_clubs.strength == 14

    def test_constuctor_card_suit(self):
        ace_of_spades = Card('A','S')
        assert ace_of_spades.card == 'A'
        assert ace_of_spades.suit == 'S'
        assert ace_of_spades.strength == 14

    def test_constuctor_bad_input(self):
        ace_of_spades = Card('Ace','Spades')
        assert 'card' not in ace_of_spades.__dict__.keys()
        assert 'suit' not in ace_of_spades.__dict__.keys() 
        assert 'strength' not in ace_of_spades.__dict__.keys()
