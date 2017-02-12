from cards import PokerHand


class TwoPairs(PokerHand):

    def __init__(self):
        self.__rating = 3

    def IsMatch(self, hand):
        tally = PokerHand.cardTally(hand)
        return len(filter(lambda x: len(x) >= 2, tally.values())) == 2

    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        pairs = sorted({k: v for (k,v) in tally.items() if len(v) == 2}.keys(), reverse=True)
        other = {k: v for (k,v) in tally.items() if len(v) == 1}.keys()
        return (self.__rating, pairs[0], pairs[1], PokerHand.Coalesce(other, 0, 0), 99, 99)
