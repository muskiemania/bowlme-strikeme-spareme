from cards import PokerHand

class Flush(PokerHand):

    def __init__(self):
        self.__rating = 6
        PokerHand.__init__(self)

    def is_match(self, hand):
        return len(self.get_suit_tally(hand).keys()) == 1 and len(hand.cards) == 5

    def get_rating(self, hand):
        hand = self.sort_cards(hand)
        strengths = [x.strength for x in hand.cards]
        return (self.__rating, strengths[0], strengths[1], strengths[2], strengths[3], strengths[4])
