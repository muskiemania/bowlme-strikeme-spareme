from cards import PokerHand, FourOfAKind, ThreeOfAKind, TwoPairs

class FullHouse(PokerHand):

    def __init__(self):
        self.__rating = 7
        PokerHand.__init__(self)

    def is_match(self, hand):
        four_of_kind = FourOfAKind().is_match(hand)
        three_of_kind = ThreeOfAKind().is_match(hand)
        two_pairs = TwoPairs().is_match(hand)
        five_cards = len(hand.cards) == 5

        return not four_of_kind and three_of_kind and two_pairs and five_cards

    def get_rating(self, hand):
        tally = self.card_tally(hand)
        inverted = {str(len(v)): k for (k, v) in tally.items()}
        return (self.__rating, inverted['3'], inverted['2'], 99, 99, 99)
