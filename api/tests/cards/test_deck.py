from cards import Card,Deck
import pytest

class Test_Deck():

    def test_constuctor_cards_none(self):
        deck = Deck()
        assert deck == Deck.generate_deck()

    def test_constructor_cards(self):
        spades_only = [card for card in Deck.generate_deck().cards if card.suit == 'S']
        
        deck = Deck(spades_only)
        assert deck.cards == spades_only

    def test_generate_deck(self):
        cards = Deck().generate_deck().cards
        assert len(cards) == 52
        for c in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            assert len([card for card in cards if card.suit == 'S' and card.card == c]) == 1
            assert len([card for card in cards if card.suit == 'D' and card.card == c]) == 1
            assert len([card for card in cards if card.suit == 'H' and card.card == c]) == 1
            assert len([card for card in cards if card.suit == 'C' and card.card == c]) == 1

    def test_shuffle_cards(self):
        cards = Deck().cards
        shuffled = Deck.shuffle_cards(Deck().cards)

        assert cards != shuffled

    def test_shuffle_deck(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle_deck()

        assert deck1 != deck2
        
    def test_show_cards(self):
        cards = ['AS','AH','AD','AC']
        aces = [Card(c) for c in cards]
        assert Deck.show_cards(aces) == cards
