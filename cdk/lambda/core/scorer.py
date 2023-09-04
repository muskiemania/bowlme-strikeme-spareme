from .poker_hand import PokerHand
from .straight_flush import StraightFlush
from .four_of_a_kind import FourOfAKind
from .full_house import FullHouse
from .flush import Flush
from .straight import Straight
from .three_of_a_kind import ThreeOfAKind
from .two_pairs import TwoPairs
from .one_pair import OnePair
from .high_card import HighCard

class Scorer:

    def __init__(self, hand):
        self.poker_hand = PokerHand(hand)
        #print self.poker_hand

    #@staticmethod
    #def default_rating():
    #    rating = (0, 0, 0, 0, 0, 0, 'Empty Hand')
    #    dto = RatingDto(rating)
    #    dto.rank = 1
    #    return dto

    def get_rating(self):
        hands = []
        hands.append(StraightFlush(self.poker_hand))
        hands.append(FourOfAKind(self.poker_hand))
        hands.append(FullHouse(self.poker_hand))
        hands.append(Flush(self.poker_hand))
        hands.append(Straight(self.poker_hand))
        hands.append(ThreeOfAKind(self.poker_hand))
        hands.append(TwoPairs(self.poker_hand))
        hands.append(OnePair(self.poker_hand))
        hands.append(HighCard(self.poker_hand))

        for hand in hands:
            if hand.is_match():
                return hand.get_rating()

#    @staticmethod
#    def score_hands(player_hands):
#        scored = []
#        for (player, hand) in player_hands:
#            hand_rating = Scorer(hand).get_rating()
#            rating = RatingDto(hand_rating, player)
#            scored.append(rating)
#            #scored.append((player, hand, rating))
#
#        return scored

    #@staticmethod
    #def rank_hands(player_hands):

    #    rating = lambda x, y: x.get()[y]
    #    sort_key = lambda x: tuple(rating(x, i) for i in range(6))
    #    sorted_hands = sorted(player_hands, key=lambda dto: sort_key(dto), reverse=True)

    #    rank = 1

    #    for rating in sorted_hands:
    #        rating.rank = rank
    #        rank += 1

    #    previous_rating = sorted_hands[0].get()
    #    previous_rank = sorted_hands[0].rank
    #    first = True
    #    for rating in sorted_hands:
    #        if first:
    #            first = False
    #            continue

    #        print str(cmp(previous_rating, rating.get()))
    #        if cmp(previous_rating, rating.get()) == 0:
    #            rating.rank = previous_rank

    #        previous_rating = rating.get()
    #        previous_rank = rating.rank

    #    return sorted_hands
