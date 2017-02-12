from cards import PokerHand
import functools


class Straight(PokerHand):

    def __init__(self):
        self.__rating = 5
        PokerHand.__init__(self)

    def IsHighStraight(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = iter(sorted(tally.keys()))
        first = next(cards)
        return 14 in tally.keys() and all(a == b for a, b in enumerate(cards, first + 1))

    def IsLowStraight(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = iter(sorted(map(lambda x: x % 13, tally.keys())))
        first = next(cards)
        return all(a == b for a, b in enumerate(cards, first + 1))

    def IsMatch(self, hand):
        return len(hand.cards) == 5 and (self.IsLowStraight(hand) or self.IsHighStraight(hand))

    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = []
        if self.IsLowStraight(hand):
            cards = sorted(map(lambda x: x % 13, tally.keys()), reverse=True)
        if self.IsHighStraight(hand):
            cards = sorted(tally.keys(), reverse=True)
        c = PokerHand.Coalesce
        return (self.__rating, c(cards, 0, 0), c(cards, 1, 0), c(cards, 2, 0), c(cards, 3, 0), c(cards, 4, 0))
