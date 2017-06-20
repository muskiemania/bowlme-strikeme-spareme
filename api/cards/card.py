class Card(object):

    def __init__(self, card=None, suit=None):

        if card is None:
            return

        card_strength = {}
        for card_number in range(2, 10):
            card_strength[str(card_number)] = card_number

            card_strength['T'] = 10
            card_strength['J'] = 11
            card_strength['Q'] = 12
            card_strength['K'] = 13
            card_strength['A'] = 14

            if len(card) == 2:
                self.card = card[0]
                self.suit = card[1]

                self.strength = 0
                if self.card in card_strength.keys():
                    self.strength = card_strength[self.card]

            if len(card) == 1 and len(suit) == 1:
                self.card = card
                self.suit = suit
                self.strength = 0
                if self.card in card_strength.keys():
                    self.strength = card_strength[self.card]

            return

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.card, self.suit) == (other.card, other.suit)

        return False
