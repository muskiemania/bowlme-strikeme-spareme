class Hand(object):

    def __init__(self, cards=None):
        self.cards = cards or []

    def show_cards(self):
        return ['%s%s' % (x.card, x.suit) for x in self.cards]
