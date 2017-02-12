from cards import PokerHand
import functools


class Straight(PokerHand):

    def __init__(self):
        self.__rating = 5
        PokerHand.__init__(self)

    def IsCoherent(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = sorted(tally.keys())
        aceLow = sorted(map(lambda x: 1 if x == 14 else x, tally.keys()))

        return (cards == range(cards[0], cards[-1]+1)) or (aceLow == range(aceLow[0], aceLow[-1]+1)) 
        
    def IsStraightToTheAce(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 13, 12, 11, 10] and self.IsCoherent(hand)
    
    def IsLowStraight(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 5, 4, 3, 2] and self.IsCoherent(hand)

    def IsMatch(self, hand):
        tally = PokerHand.cardTally(hand)
        return len(tally.keys()) == 5 and self.IsCoherent(hand)

    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        cards = []
        if self.IsLowStraight(hand):
            cards = sorted(map(lambda x: 1 if x == 14 else x, tally.keys()), reverse=True)
        elif self.IsCoherent(hand):
            cards = sorted(tally.keys(), reverse=True)
        c = PokerHand.Coalesce
        return (self.__rating, c(cards, 0, 0), c(cards, 1, 0), c(cards, 2, 0), c(cards, 3, 0), c(cards, 4, 0))
