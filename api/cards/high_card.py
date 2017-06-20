from cards import PokerHand

class HighCard(PokerHand):

    def __init__(self):
        self.__rating = 1
        PokerHand.__init__(self)

    @classmethod
    def is_match(cls, hand):
        return True or hand

    def get_rating(self, hand):
        tally = self.card_tally(hand)
        cards = sorted(tally.keys(), reverse=True) or []
        cards.extend([0, 0, 0, 0, 0])
        coalesce = self.coalesce
        coalesced = [coalesce(cards, x, 0) for x in [0, 1, 2, 3, 4]]
        return (self.__rating, coalesced[0], coalesced[1], coalesced[2], coalesced[3], coalesced[4])
