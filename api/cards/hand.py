class Hand:

    def __init__(self, cards = []):
        self.cards = cards

    def draw_cards(self, drawn_cards = []):
        for card in drawn_cards:
            self.cards.append(card)

    def discard(self, discards = []):
        for card in discards:
            if card not in self.cards:
                raise Exception('cannot discard a card not in my hand')

            i = self.cards.index(card)
            del self.cards[i]
            
    def show_cards(self):
        return map(lambda x: '%s%s' % (x.card, x.suit), self.cards)
