import unittest
import cards.card
import cards.deck

class Test_Deck(unittest.TestCase):

    def test_constuctor_cards_none(self):
        deck = cards.deck.Deck()
        self.assertEqual(deck, cards.deck.Deck.generate())

    def test_constructor_cards(self):
        spades_only = [card for card in cards.deck.Deck.generate().cards if card.suit == 'S']
        
        deck = cards.deck.Deck(spades_only)
        self.assertEqual(deck.cards, spades_only)

    def test_generate_deck(self):
        cards = cards.deck.Deck().generate().cards
        self.assertEqual(len(cards), 52)

        for c in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            self.assertEqual(len([card for card in cards if card.suit == 'S' and card.card == c]), 1)
            self.assertEqual(len([card for card in cards if card.suit == 'D' and card.card == c]), 1)
            self.assertEqual(len([card for card in cards if card.suit == 'H' and card.card == c]), 1)
            self.assertEqual(len([card for card in cards if card.suit == 'C' and card.card == c]), 1)

    def test_shuffle_cards(self):
        cards = cards.deck.Deck().cards
        shuffled = Deck.shuffle_cards(cards.deck.Deck().cards)

        self.assertNotEqual(cards, shuffled)

    def test_shuffle_deck(self):
        deck1 = cards.deck.Deck()
        deck2 = cards.deck.Deck()
        deck2.shuffle_deck()

        self.assertNotEqual(deck1, deck2)
        
    def test_show_cards(self):
        _cards = ['AS','AH','AD','AC']
        aces = [cards.card.Card(c) for c in _cards]
        self.assertEqual(Deck.show_cards(aces), cards)
