import cards.poker_hand as poker_hand

class ThreeOfAKind(poker_hand.PokerHand):

    def __init__(self, hand):
        self.__rating = 4
        self.__name = 'Three-Of-A-Kind'
        poker_hand.PokerHand.__init__(self, hand)

    def is_match(self):
        tally = self.card_tally()
        filtered = [x for x in tally.values() if len(x) == 3]
        return any(filtered)

    def get_rating(self):
        tally = self.card_tally()
        trips = list({k: v for (k, v) in tally.items() if len(v) == 3}.keys())
        others = sorted(list({k: v for (k, v) in tally.items() if len(v) < 3}.keys()), reverse=True)
        coalesce = self.coalesce

        rating = (self.__rating, trips[0], coalesce(others, 0, 0), coalesce(others, 1, 0), 99, 99, self.__name)

        if len(self.cards) == 5 and len(others) == 1:
            rating = (self.__rating, trips[0], coalesce(others, 0), 99, 99, 99, self.__name)

        return rating
