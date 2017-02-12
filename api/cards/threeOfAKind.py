from cards import PokerHand


class ThreeOfAKind(PokerHand):

    def __init__(self):
        self.__rating = 4

    def IsMatch(self, hand):
        tally = PokerHand.cardTally(hand)
        return any(filter(lambda x: len(x) == 3, tally.values()))

    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        trips = {k: v for (k,v) in tally.items() if len(v) == 3}.keys()
        others = sorted({k: v for (k,v) in tally.items() if len(v) < 3}.keys(), reverse=True)
        c = PokerHand.Coalesce
        if len(hand.cards) == 5 and len(others) == 1:
            return (self.__rating, trips[0], c(others, 0), 99, 99, 99)

        return (self.__rating, trips[0], c(others, 0, 0), c(others, 1, 0), 99, 99)
