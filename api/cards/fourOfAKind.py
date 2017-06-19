from cards import PokerHand

class FourOfAKind(PokerHand):

    def __init__(self):
        self.__rating = 8
        PokerHand.__init__(self)

    def is_match(self, hand):
        tally = PokerHand.card_tally(hand)
        return any(filter(lambda x: len(x) == 4, tally.values()))
        
    def get_rating(self, hand):
        tally = PokerHand.card_tally(hand)
        quad = {k: v for (k,v) in tally.items() if len(v) == 4}.keys()
        others = sorted({k:v for (k,v) in tally.items() if len(v) < 4}.keys(), reverse=True)
        return (self.__rating, quad[0], PokerHand.coalesce(others, 0, 0), 99, 99, 99)
