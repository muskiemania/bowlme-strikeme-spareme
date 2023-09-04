import poker_hand
import hand
import straight
import flush

class StraightFlush(poker_hand.PokerHand):

    def __init__(self, hand):
        self.__rating = 9
        self.__name = 'Straight Flush'
        poker_hand.PokerHand.__init__(self, hand)

    def is_match(self):
        return straight.Straight(hand.Hand(self.cards)).is_match() and flush.Flush(hand.Hand(self.cards)).is_match()

    def get_rating(self):
        (skip, card1, card2, card3, card4, card5, text) = straight.Straight(hand.Hand(self.cards)).get_rating()

        rating = (self.__rating, card1, card2, card3, card4, card5, self.__name)

        if self.is_royal_flush():
            rating = (self.__rating + 1, card1, card2, card3, card4, card5, 'Royal Flush')

        return rating

    def is_royal_flush(self):
        return self.is_match() and straight.Straight(hand.Hand(self.cards)).is_straight_to_the_ace()
