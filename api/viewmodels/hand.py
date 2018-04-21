
class HandModel(object):
    def __init__(self, cards):
        self.cards = self.sorted_cards(cards)

    def fromDto(self):
        return {'cards': self.cards, 'numberOfCards': len(self.cards)}

    def __get_card_order(self, card):
        order = list(card)[0]

        if order == 'T':
            return 10
        if order == 'J':
            return 11
        if order == 'Q':
            return 12
        if order == 'K':
            return 13
        if order == 'A':
            return 14

        return int(order)

    def __get_suit_order(self, card):
        order = list(card)[1]

        if order == 'C':
            return 1
        if order == 'D':
            return 2
        if order == 'H':
            return 3
        if order == 'S':
            return 4

        return 0

    def sorted_cards(self, cards):

        card_order = self.__get_card_order
        suit_order = self.__get_suit_order
        with_order = [(card, card_order(card), suit_order(card)) for card in cards]

        sort_key = lambda (x, y, z): (y, z)
        sorted_hand = sorted(with_order, key=lambda x: sort_key(x))

        return [card for (card, _, _) in sorted_hand]
