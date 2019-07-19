import cards
from bowl_redis_dto import RatingDto

class Scorer(object):

    def __init__(self, hand):
        self.poker_hand = cards.PokerHand(hand)
        #print self.poker_hand

    @staticmethod
    def default_rating():
        rating = (0, 0, 0, 0, 0, 0, 'Empty Hand')
        dto = RatingDto(rating)
        dto.rank = 1
        return dto

    def get_rating(self):
        hands = []
        hands.append(cards.StraightFlush(self.poker_hand))
        hands.append(cards.FourOfAKind(self.poker_hand))
        hands.append(cards.FullHouse(self.poker_hand))
        hands.append(cards.Flush(self.poker_hand))
        hands.append(cards.Straight(self.poker_hand))
        hands.append(cards.ThreeOfAKind(self.poker_hand))
        hands.append(cards.TwoPairs(self.poker_hand))
        hands.append(cards.OnePair(self.poker_hand))
        hands.append(cards.HighCard(self.poker_hand))

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

    @staticmethod
    def rank_hands(player_hands):

        rating = lambda x, y: x.get()[y]
        sort_key = lambda x: tuple(rating(x, i) for i in range(6))
        sorted_hands = sorted(player_hands, key=lambda dto: sort_key(dto), reverse=True)

        rank = 1

        for rating in sorted_hands:
            rating.rank = rank
            rank += 1

        previous_rating = sorted_hands[0].get()
        previous_rank = sorted_hands[0].rank
        first = True
        for rating in sorted_hands:
            if first:
                first = False
                continue

            print(str(cmp(previous_rating, rating.get())))
            if cmp(previous_rating, rating.get()) == 0:
                rating.rank = previous_rank

            previous_rating = rating.get()
            previous_rank = rating.rank

        return sorted_hands
