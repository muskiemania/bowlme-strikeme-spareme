import cards.poker_hand as poker_hand
import cards.hand
import cards.straight
import cards.flush

class StraightFlush(poker_hand.PokerHand):

    def __init__(self, hand):
        self.__rating = 9
        self.__name = 'Straight Flush'
        poker_hand.PokerHand.__init__(self, hand)

    def is_match(self):
        return cards.straight.Straight(cards.hand.Hand(self.cards)).is_match() and cards.flush.Flush(cards.hand.Hand(self.cards)).is_match()

    def get_rating(self):
        (skip, card1, card2, card3, card4, card5, text) = cards.straight.Straight(cards.hand.Hand(self.cards)).get_rating().get()

        rating = (self.__rating, card1, card2, card3, card4, card5, self.__name)

        if self.is_royal_flush():
            rating = (self.__rating + 1, card1, card2, card3, card4, card5, 'Royal Flush')

        return rating

    def is_royal_flush(self):
        return self.is_match() and cards.straight.Straight(cards.hand.Hand(self.cards)).is_straight_to_the_ace()
