from cards import PokerHand

class FourOfAKind(PokerHand):

    def __init__(self, hand):
        self.__rating = 8
        PokerHand.__init__(self, hand)

    def is_match(self):
        tally = self.card_tally()
        return any([True for x in tally.values() if len(x) == 4])

    def get_rating(self):
        tally = self.card_tally()
        quad = {k: v for (k, v) in tally.items() if len(v) == 4}.keys()
        others = sorted({k:v for (k, v) in tally.items() if len(v) < 4}.keys(), reverse=True)
        return (self.__rating, quad[0], self.coalesce(others, 0, 0), 99, 99, 99)
