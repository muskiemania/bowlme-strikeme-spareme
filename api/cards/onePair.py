from cards import PokerHand


class OnePair(PokerHand):

    def __init__(self):
        self.__rating = 2

    def IsMatch(self, hand):
        tally = PokerHand.cardTally(hand)
        return len(filter(lambda x: len(x) == 2, tally.values())) == 1

    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        pair = {k: v for (k,v) in tally.items() if len(v) == 2}.keys()
        print pair
        others = sorted({k: v for (k,v) in tally.items() if len(v) != 2}.keys(), reverse=True)
        c = PokerHand.Coalesce
        return (self.__rating, pair[0], c(others, 0, 0), c(others, 1, 0), c(others, 2, 0), 99) 
