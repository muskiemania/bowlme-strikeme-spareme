from cards import PokerHand, Straight, Flush


class StraightFlush(PokerHand, Straight, Flush):

    def __init__(self):
        self.__rating = 9
        Straight.__init__(self)
        Flush.__init__(self)

    def IsMatch(self, hand):
        return Straight.IsMatch(self, hand) and Flush.IsMatch(self, hand)

    def GetRating(self, hand):
        (r,c1,c2,c3,c4,c5) = Straight().GetRating(hand)
        
        if self.IsRoyalFlush(hand):
            return (self.__rating + 1, c1, c2, c3, c4, c5)
        
        return (self.__rating, c1, c2, c3, c4, c5)

    def IsRoyalFlush(self, hand):
        return self.IsMatch(hand) and Straight.IsHighStraight(self, hand)
