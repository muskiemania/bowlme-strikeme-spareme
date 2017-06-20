from cards import PokerHand


class ThreeOfAKind(PokerHand):

    def __init__(self):
        self.__rating = 4
        PokerHand.__init__(self)

    def is_match(self, hand):
        tally = self.card_tally(hand)
        filtered = [x for x in tally.values() if len(x) == 3]
        return any(filtered)

    def get_rating(self, hand):
        tally = self.card_tally(hand)
        trips = {k: v for (k, v) in tally.items() if len(v) == 3}.keys()
        others = sorted({k: v for (k, v) in tally.items() if len(v) < 3}.keys(), reverse=True)
        coalesce = self.coalesce
        if len(hand.cards) == 5 and len(others) == 1:
            return (self.__rating, trips[0], coalesce(others, 0), 99, 99, 99)

        return (self.__rating, trips[0], coalesce(others, 0, 0), coalesce(others, 1, 0), 99, 99)
