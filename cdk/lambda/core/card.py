
class Card:

    def __init__(self, card=None, suit=None):

        if card is None:
            return

        card_and_suit = self.__get_card_and_suit(card, suit)
        if card_and_suit is not None:
            (card, suit) = card_and_suit
            if card:
                self.card = card
                self.strength = self.__get_strength()
                self.card_display = self.__get_card_display()
                
            if suit:
                self.suit = suit
                self.suit_name = self.__get_suit_display()

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

    def __get_card_display(self):
        return str(self.card) if self.card != 'T' else '10'
        
    def __get_suit_display(self):
        suits = {}
        suits['C'] = 'clubs'
        suits['D'] = 'diamonds'
        suits['H'] = 'hearts'
        suits['S'] = 'spades'
        return suits[self.suit]
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.card, self.suit) == (other.card, other.suit)

        return False
