import cards.poker_hand as poker_hand
import cards.four_of_a_kind as four
import cards.three_of_a_kind as three
import cards.two_pairs as two
import cards.hand as hand

class FullHouse(poker_hand.PokerHand):

    def __init__(self, hand):
        self.__rating = 7
        self.__name = 'Full House'
        poker_hand.PokerHand.__init__(self, hand)

    def is_match(self):
        four_of_kind = four.FourOfAKind(hand.Hand(self.cards)).is_match()
        three_of_kind = three.ThreeOfAKind(hand.Hand(self.cards)).is_match()
        two_pairs = two.TwoPairs(hand.Hand(self.cards)).is_match()
        five_cards = len(self.cards) == 5

        return not four_of_kind and three_of_kind and two_pairs and five_cards

    def get_rating(self):
        tally = self.card_tally()
        inverted = {str(len(v)): k for (k, v) in tally.items()}
        rating = (self.__rating, inverted['3'], inverted['2'], 99, 99, 99, self.__name)
        return rating
