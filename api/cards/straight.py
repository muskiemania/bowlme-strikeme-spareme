from cards import PokerHand

class Straight(PokerHand):

    def __init__(self):
        self.__rating = 5
        PokerHand.__init__(self)

    def is_coherent(self, hand):
        tally = self.card_tally(hand)
        cards = sorted(tally.keys())
        ace_low = sorted([1 if k == 14 else k for k in tally.iterkeys()])

        low_straight = (ace_low == range(ace_low[0], ace_low[-1]+1))
        regular_straight = (cards == range(cards[0], cards[-1]+1))
        return regular_straight or low_straight

    def is_straight_to_the_ace(self, hand):
        tally = self.card_tally(hand)
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 13, 12, 11, 10] and self.is_coherent(hand)

    def is_low_straight(self, hand):
        tally = self.card_tally(hand)
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 5, 4, 3, 2] and self.is_coherent(hand)

    def is_match(self, hand):
        tally = self.card_tally(hand)
        return len(tally.keys()) == 5 and self.is_coherent(hand)

    def get_rating(self, hand):
        tally = self.card_tally(hand)
        cards = []
        if self.is_low_straight(hand):
            cards = sorted([1 if k == 14 else k for k in tally.iterkeys()], reverse=True)
        elif self.is_coherent(hand):
            cards = sorted(tally.keys(), reverse=True)
        coalesced = [self.coalesce(cards, x, 0) for x in [0, 1, 2, 3, 4]]
        return (self.__rating, coalesced[0], coalesced[1], coalesced[2], coalesced[3], coalesced[4])
