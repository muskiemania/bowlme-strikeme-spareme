from cards import PokerHand, Straight, Flush

class StraightFlush(PokerHand):

    def __init__(self, hand):
        self.__rating = 9
        PokerHand.__init__(self, hand)

    def is_match(self):
        return Straight(self.hand).is_match() and Flush(self.hand).is_match()

    def get_rating(self):
        (_, card1, card2, card3, card4, card5) = Straight(self.hand).get_rating()

        if self.is_royal_flush():
            return (self.__rating + 1, card1, card2, card3, card4, card5)

        return (self.__rating, card1, card2, card3, card4, card5)

    def is_royal_flush(self):
        return self.is_match() and Straight(self.hand).is_straight_to_the_ace()
