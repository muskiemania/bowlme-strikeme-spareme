
class HandModel(object):
    def __init__(self, cards):
        self.cards = cards

    def fromDto(self):
        return {'cards': self.cards, 'numberOfCards': len(self.cards)}
