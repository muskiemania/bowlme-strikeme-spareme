class Hand:

    def __init__(self, cards = []):
        self.cards = cards

    def DrawCards(self, drawnCards = []):
        for card in drawnCards:
            self.cards.append(card)

    def Discard(self, discards = []):
        for card in discards:
            if card not in self.cards:
                raise Exception('cannot discard a card not in my hand')

            i = self.cards.index(card)
            del self.cards[i]
            
    def ShowCards(self):
        return map(lambda x: '%s%s' % (x.card, x.suit), self.cards)
