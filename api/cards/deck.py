from cards import Card
import itertools
from random import randint

class Deck:

    def __init__(self, cards=None):
        if cards == None:
            self.cards = self.GenerateDeck()
        else:
            self.cards = cards

    def GenerateDeck(self):
        cards = [str(x) for x in range(2,10)]
        cards += ['T','J','Q','K','A']

        suits = ['C','S','H','D']

        pairs = itertools.product(cards,suits)
        deck = map(lambda (card,suit): Card(card,suit), pairs)
        return deck

    @staticmethod
    def ShuffleCards(cards):
        for i in range(0, len(cards)-2):
            j = randint(i, len(cards)-1)
            cards[i], cards[j] = cards[j], cards[i]
        return cards
    
    @staticmethod
    def ShowCards(cards):
        return map(lambda x: "%s%s" % (x.card,x.suit), cards)

    def ShuffleDeck(self):
        self.cards = ShuffleCards(self.cards)
        return
    

    def GetDeck(self):
        return self.cards

            
        
    
