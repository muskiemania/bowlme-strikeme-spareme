from cards import Hand, PokerHand, FourOfAKind, ThreeOfAKind, TwoPairs

class FullHouse(PokerHand):

    def __init__(self, hand):
        self.__rating = 7
        self.__name = 'Full House'
        PokerHand.__init__(self, hand)

    def is_match(self):
        four_of_kind = FourOfAKind(Hand(self.cards)).is_match()
        three_of_kind = ThreeOfAKind(Hand(self.cards)).is_match()
        two_pairs = TwoPairs(Hand(self.cards)).is_match()
        five_cards = len(self.cards) == 5

        return not four_of_kind and three_of_kind and two_pairs and five_cards

    def get_rating(self):
        tally = self.card_tally()
        inverted = {str(len(v)): k for (k, v) in tally.items()}
        return (self.__rating, inverted['3'], inverted['2'], 99, 99, 99, self.__name)
