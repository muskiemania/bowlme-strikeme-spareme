from cards import PokerHand


class OnePair(PokerHand):

    def __init__(self):
        self.__rating = 2

    def is_match(self, hand):
        tally = PokerHand.card_tally(hand)
        return len(filter(lambda x: len(x) == 2, tally.values())) == 1

    def get_rating(self, hand):
        tally = PokerHand.card_tally(hand)
        pair = {k: v for (k,v) in tally.items() if len(v) == 2}.keys()
        others = sorted({k: v for (k,v) in tally.items() if len(v) != 2}.keys(), reverse=True)
        c = PokerHand.coalesce
        return (self.__rating, pair[0], c(others, 0, 0), c(others, 1, 0), c(others, 2, 0), 99) 
