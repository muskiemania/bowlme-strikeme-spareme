from cards import PokerHand, Straight, Flush

class StraightFlush(PokerHand):

    def __init__(self):
        self.__rating = 9
        PokerHand.__init__(self)

    def is_match(self, hand):
        return Straight().is_match(hand) and Flush().is_match(hand)

    def get_rating(self, hand):
        (_, card1, card2, card3, card4, card5) = Straight().get_rating(hand)

        if self.is_royal_flush(hand):
            return (self.__rating + 1, card1, card2, card3, card4, card5)

        return (self.__rating, card1, card2, card3, card4, card5)

    def is_royal_flush(self, hand):
        return self.is_match(hand) and Straight().is_straight_to_the_ace(hand)
