from cards import PokerHand, FourOfAKind, ThreeOfAKind, TwoPairs

class FullHouse(PokerHand, FourOfAKind, ThreeOfAKind, TwoPairs):

    def __init__(self):
        self.__rating = 7
        FourOfAKind.__init__(self)
        ThreeOfAKind.__init__(self)
        TwoPairs.__init__(self)

    def IsMatch(self, hand):
        return not FourOfAKind.IsMatch(self, hand) and ThreeOfAKind.IsMatch(self, hand) and TwoPairs.IsMatch(self, hand) and len(hand.cards) == 5

    def GetRating(self, hand):
        tally = PokerHand.cardTally(hand)
        inverted = {str(len(v)): k for (k,v) in tally.items()}
        return (self.__rating, inverted['3'], inverted['2'], 99, 99, 99)
