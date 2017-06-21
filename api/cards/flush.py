from cards import PokerHand

class Flush(PokerHand):

    def __init__(self, hand):
        self.__rating = 6
        PokerHand.__init__(self, hand)

    def is_match(self):
        return len(self.get_suit_tally(self.hand).keys()) == 1 and len(self.hand.cards) == 5

    def get_rating(self):
        self.sort_cards()
        strengths = [x.strength for x in self.hand.cards]
        return (self.__rating, strengths[0], strengths[1], strengths[2], strengths[3], strengths[4])
