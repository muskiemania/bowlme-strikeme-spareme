from cards import Hand, PokerHand, Straight, Flush
from bowl_redis_dto import RatingDto

class StraightFlush(PokerHand):

    def __init__(self, hand):
        self.__rating = 9
        self.__name = 'Straight Flush'
        PokerHand.__init__(self, hand)

    def is_match(self):
        return Straight(Hand(self.cards)).is_match() and Flush(Hand(self.cards)).is_match()

    def get_rating(self):
        (skip, card1, card2, card3, card4, card5, text) = Straight(Hand(self.cards)).get_rating().get()

        rating = (self.__rating, card1, card2, card3, card4, card5, self.__name)

        if self.is_royal_flush():
            rating = (self.__rating + 1, card1, card2, card3, card4, card5, 'Royal Flush')

        return RatingDto(rating)

    def is_royal_flush(self):
        return self.is_match() and Straight(Hand(self.cards)).is_straight_to_the_ace()
