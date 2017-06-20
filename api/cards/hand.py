class Hand(object):

    def __init__(self, cards=None):
        self.cards = cards or []

    def draw_cards(self, drawn_cards=None):
        for card in drawn_cards or []:
            self.cards.append(card)

    def discard(self, discards=None):
        for card in discards or []:
            if card not in self.cards:
                raise Exception('cannot discard a card not in my hand')

            i = self.cards.index(card)
            del self.cards[i]

    def show_cards(self):
        return ['%s%s' % (x.card, x.suit) for x in self.cards]
