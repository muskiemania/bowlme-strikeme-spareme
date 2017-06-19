"""Handles detecting and scoring poker hands that are rated as Two Pair"""

from cards import PokerHand


class TwoPairs(PokerHand):
    """Handles detecting and scoring poker hands that are ratd as TwoPair"""

    def __init__(self):
        self.__rating = 3

    def is_match(self, hand):
        tally = PokerHand.card_tally(hand)
        return len(filter(lambda x: len(x) >= 2, tally.values())) == 2

    def get_rating(self, hand):
        tally = PokerHand.card_tally(hand)
        pairs = sorted({k: v for (k, v) in tally.items() if len(v) == 2}.keys(), reverse=True)
        other = {k: v for (k, v) in tally.items() if len(v) == 1}.keys()
        return (self.__rating, pairs[0], pairs[1], PokerHand.coalesce(other, 0, 0), 99, 99)
