class Card(object):

    def __init__(self, card=None, suit=None):

        if card is None:
            return

        card_and_suit = self.__get_card_and_suit(card, suit)
        if card_and_suit is not None:
            (card, suit) = card_and_suit
            if card:
                self.card = card
                self.strength = self.__get_strength()

            if suit:
                self.suit = suit

    def __get_card_and_suit(self, card, suit=None):

        if len(card) == 2:
            return (card[0], card[1])
        elif len(card) == 1 and len(suit) == 1:
            return (card, suit)

        return (None, None)

    def __get_strength(self):
        card_strength = {}
        card_strength['T'] = 10
        card_strength['J'] = 11
        card_strength['Q'] = 12
        card_strength['K'] = 13
        card_strength['A'] = 14

        if self.card in card_strength.keys():
            return card_strength[self.card]

        try:
            strength = int(self.card)
        except:
            return 0
        
        if strength in range(2, 10):
            return strength

        return 0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.card, self.suit) == (other.card, other.suit)

        return False
