import unittest
import cards.card

class Test_Card(unittest.TestCase):

    def test_get_card_and_suit_card_and_suit_no_suit(self):
        (card, suit) = cards.card.Card()._Card__get_card_and_suit('JH')
        self.assertEqual(card, 'J')
        self.assertEqual(suit, 'H')

    def test_get_card_and_suit_card_and_suit(self):
        (card, suit) = cards.card.Card()._Card__get_card_and_suit('A', 'D')
        self.assertEqual(card, 'A')
        self.assertEqual(suit, 'D')

    def test_get_card_and_suit_invalid_card(self):
        (card, suit) = cards.card.Card()._Card__get_card_and_suit('Ace', 'Spades')
        self.assertIsNone(card)
        self.assertIsNone(suit)

    def test_get_strength(self):
        self.assertEqual(cards.card.Card('2H')._Card__get_strength(), 2)
        self.assertEqual(cards.card.Card('3H')._Card__get_strength(), 3)
        self.assertEqual(cards.card.Card('4H')._Card__get_strength(), 4)
        self.assertEqual(cards.card.Card('5H')._Card__get_strength(), 5)
        self.assertEqual(cards.card.Card('6H')._Card__get_strength(), 6)
        self.assertEqual(cards.card.Card('7H')._Card__get_strength(), 7)
        self.assertEqual(cards.card.Card('8H')._Card__get_strength(), 8)
        self.assertEqual(cards.card.Card('9H')._Card__get_strength(), 9)
        self.assertEqual(cards.card.Card('TH')._Card__get_strength(), 10)
        self.assertEqual(cards.card.Card('JH')._Card__get_strength(), 11)
        self.assertEqual(cards.card.Card('QH')._Card__get_strength(), 12)
        self.assertEqual(cards.card.Card('KH')._Card__get_strength(), 13)
        self.assertEqual(cards.card.Card('AH')._Card__get_strength(), 14)
        
    def test_eq1(self):
        first_card = cards.card.Card('JH')
        second_card = cards.card.Card('JH')
        self.assertEqual(first_card, second_card)

    def test_eq2(self):
        third_card = cards.card.Card('4', 'D')
        fourth_card = cards.card.Card('4D')
        self.assertEqual(third_card, fourth_card)
    
    def test_constuctor_suit_none1(self):
        ace_of_hearts = cards.card.Card('AH')
        self.assertEqual(ace_of_hearts.card, 'A')
        self.assertEqual(ace_of_hearts.suit, 'H')
        self.assertEqual(ace_of_hearts.strength, 14)

    def test_constuctor_suit_none2(self):
        three_of_hearts = cards.card.Card('3H')
        self.assertEqual(three_of_hearts.card, '3')
        self.assertEqual(three_of_hearts.suit, 'H')
        self.assertEqual(three_of_hearts.strength, 3)
        
    def test_constuctor_card2_suit(self):
        ace_of_clubs = cards.card.Card('AC','S')
        self.assertEqual(ace_of_clubs.card, 'A')
        self.assertEqual(ace_of_clubs.suit, 'C')
        self.assertEqual(ace_of_clubs.strength, 14)

    def test_constuctor_card_suit(self):
        ace_of_spades = cards.card.Card('A','S')
        self.assertEqual(ace_of_spades.card, 'A')
        self.assertEqual(ace_of_spades.suit, 'S')
        self.assertEqual(ace_of_spades.strength, 14)

    def test_constuctor_bad_input(self):
        ace_of_spades = cards.card.Card('Ace','Spades')
        self.assertNotIn('card', ace_of_spades.__dict__.keys())
        self.assertNotIn('suit', ace_of_spades.__dict__.keys())
        self.assertNotIn('strength', ace_of_spades.__dict__.keys())
