import itertools
from random import randint
import cards.card

class Deck:

    def __init__(self, cards=None):
        self._cards = cards

    def cards(self):
        return [f'{c.card}{c.suit}' for c in self._cards]

    @staticmethod
    def generate(number_of_decks=1):
        cards = [str(x) for x in range(2, 10)]
        
        cards += ['T', 'J', 'Q', 'K', 'A']
        suits = ['C', 'S', 'H', 'D']

        pairs = itertools.product(cards, suits)
        pairs = list(pairs) * number_of_decks
        deck = Deck(cards=[cards.card.Card(card, suit) for (card, suit) in pairs])
        
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
        self.cards = Deck.shuffle_cards(self._cards)
        return

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.cards == other.cards
