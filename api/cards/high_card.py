from cards import PokerHand
from bowl_redis_dto import RatingDto

class HighCard(PokerHand):

    def __init__(self, hand):
        self.__rating = 1
        self.__name = 'High Card'
        PokerHand.__init__(self, hand)

    def is_match(self):
        return True

    def get_rating(self):
        tally = self.card_tally()
        cards = sorted(tally.keys(), reverse=True) or []
        cards.extend([0, 0, 0, 0, 0])
        coalesce = self.coalesce
        coalesced = [coalesce(cards, x, 0) for x in [0, 1, 2, 3, 4]]
        rating = (self.__rating, coalesced[0], coalesced[1], coalesced[2], coalesced[3], coalesced[4], self.__name)
        return RatingDto(rating)
