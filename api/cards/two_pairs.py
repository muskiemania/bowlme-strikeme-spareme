from cards import PokerHand

class TwoPairs(PokerHand):

    def __init__(self, hand):
        self.__rating = 3
        self.__name = 'Two Pairs'
        PokerHand.__init__(self, hand)

    def is_match(self):
        tally = self.card_tally()
        return len([x for x in tally.values() if len(x) >= 2]) == 2

    def get_rating(self):
        tally = self.card_tally()
        pairs = sorted({k: v for (k, v) in tally.items() if len(v) == 2}.keys(), reverse=True)
        other = {k: v for (k, v) in tally.items() if len(v) == 1}.keys()
        rating = (self.__rating, pairs[0], pairs[1], self.coalesce(other, 0, 0), 99, 99, self.__name)
        return RatingDto(rating)
