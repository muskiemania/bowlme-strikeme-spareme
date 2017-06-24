import itertools
from random import randint
from cards import Card

class Deck(object):

    def __init__(self, cards=None):
        if cards is None:
            self.cards = Deck.generate_deck().cards
        else:
            self.cards = cards

    @staticmethod
    def generate_deck():
        cards = [str(x) for x in range(2, 10)]
        cards += ['T', 'J', 'Q', 'K', 'A']

        suits = ['C', 'S', 'H', 'D']

        pairs = itertools.product(cards, suits)
        deck = Deck(cards=[Card(card, suit) for (card, suit) in pairs])
        return deck

    @staticmethod
    def shuffle_cards(cards):
        for i in range(0, len(cards)-2):
            j = randint(i, len(cards)-1)
            cards[i], cards[j] = cards[j], cards[i]
        return cards

    @staticmethod
    def show_cards(cards):
        return ["%s%s" % (x.card, x.suit) for x in cards]

    def shuffle_deck(self):
        self.cards = Deck.shuffle_cards(self.cards)
        return

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.cards == other.cards
