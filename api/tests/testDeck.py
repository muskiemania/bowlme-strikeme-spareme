from cards import Card,Deck
import pytest

class Test_Deck():

    def test_constuctor_cards_none(self):
        deck = Deck()
        assert deck.cards == Deck().generate_deck()

    def test_constructor_cards(self):
        spades_only = filter(lambda x: x.suit == 'S', Deck().generate_deck())

        deck = Deck(spades_only)
        assert deck.cards == spades_only

    def test_generate_deck(self):
        cards = Deck().generate_deck()
        assert len(cards) == 52
        for c in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            assert len(filter(lambda x: x.suit == 'S' and x.card == c, cards)) == 1
            assert len(filter(lambda x: x.suit == 'H' and x.card == c, cards)) == 1
            assert len(filter(lambda x: x.suit == 'D' and x.card == c, cards)) == 1
            assert len(filter(lambda x: x.suit == 'C' and x.card == c, cards)) == 1

    def test_shuffle(self):
        deck = Deck().get_deck()
        clone = list(deck)
        shuffled = Deck.shuffle_cards(clone)

        assert Deck.show_cards(deck) != Deck.show_cards(shuffled)
        
    def test_get_deck(self):
        deck = Deck()
        assert deck.cards == deck.get_deck()

    def test_show_cards(self):
        cards = ['AS','AH','AD','AC']
        aces = map(lambda x: Card(x), cards)
        assert Deck.show_cards(aces) == cards
