from cards import PokerHand, Straight, Flush


class StraightFlush(PokerHand, Straight, Flush):

    def __init__(self):
        self.__rating = 9
        Straight.__init__(self)
        Flush.__init__(self)

    def is_match(self, hand):
        return Straight.is_match(self, hand) and Flush.is_match(self, hand)

    def get_rating(self, hand):
        (r,c1,c2,c3,c4,c5) = Straight.get_rating(self,hand)
        
        if self.is_royal_flush(hand):
            return (self.__rating + 1, c1, c2, c3, c4, c5)
        
        return (self.__rating, c1, c2, c3, c4, c5)

    def is_royal_flush(self, hand):
        return self.is_match(hand) and Straight.is_straight_to_the_ace(self, hand)
