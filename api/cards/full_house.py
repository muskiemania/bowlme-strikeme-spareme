from cards import PokerHand, FourOfAKind, ThreeOfAKind, TwoPairs

class FullHouse(PokerHand):

    def __init__(self, hand):
        self.__rating = 7
        PokerHand.__init__(self, hand)

    def is_match(self):
        four_of_kind = FourOfAKind(self.hand).is_match()
        three_of_kind = ThreeOfAKind(self.hand).is_match()
        two_pairs = TwoPairs(self.hand).is_match()
        five_cards = len(self.hand.cards) == 5

        return not four_of_kind and three_of_kind and two_pairs and five_cards

    def get_rating(self):
        tally = self.card_tally()
        inverted = {str(len(v)): k for (k, v) in tally.items()}
        return (self.__rating, inverted['3'], inverted['2'], 99, 99, 99)
