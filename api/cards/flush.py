from cards import PokerHand

class Flush(PokerHand):

    def __init__(self, hand):
        self.__rating = 6
        self.__name = 'Flush'
        PokerHand.__init__(self, hand)

    def is_match(self):
        return len(self.get_suit_tally().keys()) == 1 and len(self.cards) == 5

    def get_rating(self):
        self.sort_cards()
        strengths = [x.strength for x in self.cards]
        rating = (self.__rating, strengths[0], strengths[1], strengths[2], strengths[3], strengths[4], self.__name)
        return RatingDto(rating)
