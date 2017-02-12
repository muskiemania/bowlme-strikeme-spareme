from cards import PokerHand

class FourOfAKind(PokerHand):

    def __init__(self):
        self.__rating = 8
        PokerHand.__init__(self)

    def IsMatch(self, hand):
        tally = PokerHand.cardTally(hand)
        return any(filter(lambda x: len(x) == 4, tally.values()))
        
    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        quad = {k: v for (k,v) in tally.items() if len(v) == 4}.keys()
        others = sorted({k:v for (k,v) in tally.items() if len(v) < 4}.keys(), reverse=True)
        return (self.__rating, quad[0], PokerHand.Coalesce(others, 0, 0), 99, 99, 99)
