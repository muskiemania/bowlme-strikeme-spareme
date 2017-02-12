from cards import Card,Deck
import pytest

class Test_Deck():

    def test_constuctor_cards_none(self):
        deck = Deck()
        assert deck.cards == Deck().GenerateDeck()

    def test_constructor_cards(self):
        spadesOnly = filter(lambda x: x.suit == 'S', Deck().GenerateDeck())

        deck = Deck(spadesOnly)
        assert deck.cards == spadesOnly

    def test_generate_deck(self):
        cards = Deck().GenerateDeck()
        assert len(cards) == 52
        for c in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            assert len(filter(lambda x: x.suit == 'S' and x.card == c, cards)) == 1
            assert len(filter(lambda x: x.suit == 'H' and x.card == c, cards)) == 1
            assert len(filter(lambda x: x.suit == 'D' and x.card == c, cards)) == 1
            assert len(filter(lambda x: x.suit == 'C' and x.card == c, cards)) == 1

    def test_shuffle(self):
        deck = Deck().GetDeck()
        clone = list(deck)
        shuffled = Deck.ShuffleCards(clone)

        assert Deck.ShowCards(deck) != Deck.ShowCards(shuffled)
        
    def test_get_deck(self):
        deck = Deck()
        assert deck.cards == deck.GetDeck()

    def test_show_cards(self):
        cards = ['AS','AH','AD','AC']
        aces = map(lambda x: Card(x), cards)
        assert Deck.ShowCards(aces) == cards
