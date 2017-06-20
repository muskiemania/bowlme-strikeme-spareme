from cards import PokerHand


class TwoPairs(PokerHand):

    def __init__(self):
        self.__rating = 3
        PokerHand.__init__(self)

    def is_match(self, hand):
        tally = self.card_tally(hand)
        return len([x for x in tally.values() if len(x) >= 2]) == 2

    def get_rating(self, hand):
        tally = self.card_tally(hand)
        pairs = sorted({k: v for (k, v) in tally.items() if len(v) == 2}.keys(), reverse=True)
        other = {k: v for (k, v) in tally.items() if len(v) == 1}.keys()
        return (self.__rating, pairs[0], pairs[1], self.coalesce(other, 0, 0), 99, 99)
