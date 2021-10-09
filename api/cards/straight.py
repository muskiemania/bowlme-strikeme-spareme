import cards.poker_hand as poker_hand

class Straight(poker_hand.PokerHand):

    def __init__(self, hand):
        self.__rating = 5
        self.__name = 'Straight'
        poker_hand.PokerHand.__init__(self, hand)

    def is_coherent(self):
        tally = self.card_tally()
        cards = sorted(tally.keys())
        ace_low = sorted([1 if k == 14 else k for k in tally.iterkeys()])

        low_straight = (ace_low == range(ace_low[0], ace_low[-1]+1))
        regular_straight = (cards == range(cards[0], cards[-1]+1))
        return regular_straight or low_straight

    def is_straight_to_the_ace(self):
        tally = self.card_tally()
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 13, 12, 11, 10] and self.is_coherent()

    def is_low_straight(self):
        tally = self.card_tally()
        cards = sorted(tally.keys(), reverse=True)
        return cards == [14, 5, 4, 3, 2] and self.is_coherent()

    def is_match(self):
        tally = self.card_tally()
        return len(tally.keys()) == 5 and self.is_coherent()

    def get_rating(self):
        tally = self.card_tally()
        cards = []
        if self.is_low_straight():
            cards = sorted([1 if k == 14 else k for k in tally.iterkeys()], reverse=True)
        elif self.is_coherent():
            cards = sorted(tally.keys(), reverse=True)
        coalesced = [self.coalesce(cards, x, 0) for x in [0, 1, 2, 3, 4]]
        rating = (self.__rating, coalesced[0], coalesced[1], coalesced[2], coalesced[3], coalesced[4], self.__name)
        return rating
