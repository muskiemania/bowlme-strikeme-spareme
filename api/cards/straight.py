from cards import PokerHand
import functools


class Straight(PokerHand):

    def __init__(self):
        self.__rating = 5
        PokerHand.__init__(self)

    def is_coherent(self, hand):
        tally = PokerHand.card_tally(hand)
        cards = sorted(tally.keys())
        ace_low = sorted(map(lambda x: 1 if x == 14 else x, tally.keys()))

        return (cards == range(cards[0], cards[-1]+1)) or (ace_low == range(ace_low[0], ace_low[-1]+1)) 
        
    def is_straight_to_the_ace(self, hand):
        tally = PokerHand.card_tally(hand)
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 13, 12, 11, 10] and self.is_coherent(hand)
    
    def is_low_straight(self, hand):
        tally = PokerHand.card_tally(hand)
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 5, 4, 3, 2] and self.is_coherent(hand)

    def is_match(self, hand):
        tally = PokerHand.card_tally(hand)
        return len(tally.keys()) == 5 and self.is_coherent(hand)

    def get_rating(self, hand):
        tally = PokerHand.card_tally(hand)
        cards = []
        if self.is_low_straight(hand):
            cards = sorted(map(lambda x: 1 if x == 14 else x, tally.keys()), reverse=True)
        elif self.is_coherent(hand):
            cards = sorted(tally.keys(), reverse=True)
        c = PokerHand.coalesce
        return (self.__rating, c(cards, 0, 0), c(cards, 1, 0), c(cards, 2, 0), c(cards, 3, 0), c(cards, 4, 0))
