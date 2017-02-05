
class Card:

        def __init__(self, card=None, suit=None):

                if card == None:
                        return

                if len(card) == 2:
                        self.card = card[0]
                        self.suit = card[1]
                        return
                        
                if len(card) == 1 and len(suit) == 1:
                        self.card = card
                        self.suit = suit
                        
                return

        def __eq__(self, other):
                if isinstance(other, self.__class__):
                        return (self.card, self.suit) == (other.card, other.suit)
                else:
                        return False
