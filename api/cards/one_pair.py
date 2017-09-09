from cards import PokerHand

class OnePair(PokerHand):

    def __init__(self, hand):
        self.__rating = 2
        PokerHand.__init__(self, hand)

    def is_match(self):
        tally = self.card_tally()
        return len([True for x in tally.values() if len(x) == 2]) == 1

    def get_rating(self):
        tally = self.card_tally()
        pair = {k: v for (k, v) in tally.items() if len(v) == 2}.keys()
        others = sorted({k: v for (k, v) in tally.items() if len(v) != 2}.keys(), reverse=True)
        coalesce = self.coalesce
        coalesced = [coalesce(others, x, 0) for x in [0, 1, 2]]
        return (self.__rating, pair[0], coalesced[0], coalesced[1], coalesced[2], 99)
