import cards
from bowl_redis_dto import GameStatus, RatingDto

class Scorer(object):

    def __init__(self, hand):
        self.poker_hand = cards.PokerHand(hand)
        #print self.poker_hand

    @staticmethod
    def default_rating():
        rating = (0, 0, 0, 0, 0, 0, 'Empty Hand')
        return RatingDto(rating)
        
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

    @staticmethod
    def score_hands(player_hands):
        scored = []
        for (player, hand) in player_hands:
            hand_rating = Scorer(hand).get_rating()
            rating = RatingDto(hand_rating, player)
            scored.append(rating)
            #scored.append((player, hand, rating))

        return scored

    @staticmethod
    def rank_hands(player_hands):
        for item in range(5, -1, -1):
            player_hands.sort(key=lambda (p, h, r): r[item], reverse=True)

        ranked = []
        index = 0
        current_rank = 1

        for (player, hand, score) in player_hands:
            if index == 0:
                ranked.append((player, hand, score, current_rank))
                index += 1
            else:
                if score != ranked[index - 1][2]:
                    current_rank += 1

                ranked.append((player, hand, score, current_rank))
                index += 1

        return ranked
