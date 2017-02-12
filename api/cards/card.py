

class Card:

        def __init__(self, card=None, suit=None):

                if card == None:
                        return

                cardStrength = {}
                for x in range(2,10):
                        cardStrength[str(x)] = x

                cardStrength['T'] = 10
                cardStrength['J'] = 11
                cardStrength['Q'] = 12
                cardStrength['K'] = 13
                cardStrength['A'] = 14

                if len(card) == 2:
                        self.card = card[0]
                        self.suit = card[1]
                        self.strength = cardStrength[self.card] if self.card in cardStrength.keys() else 0
                        
                if len(card) == 1 and len(suit) == 1:
                        self.card = card
                        self.suit = suit
                        self.strength = cardStrength[self.card] if self.card in cardStrength.keys() else 0
                        
                return

        def __eq__(self, other):
                if isinstance(other, self.__class__):
                        return (self.card, self.suit) == (other.card, other.suit)
                else:
                        return False
