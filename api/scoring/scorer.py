import cards
from entities import GameStatus

class Scorer(object):

    def __init__(self, game_status, player_status, player_hand):
        self.game_status = game_status
        self.player_status = player_status
        self.poker_hand = cards.PokerHand(player_hand)

    def get_rating(self):
        if self.game_status is not GameStatus.FINISHED:
            hand = cards.HighCard(self.poker_hand)
            return hand.get_rating()

        hands = []
        hands.append(cards.StraightFlush(poker_hand))
        hands.append(cards.FourOfAKind(poker_hand))
        hands.append(cards.FullHouse(poker_hand))
        hands.append(cards.Flush(poker_hand))
        hands.append(cards.Straight(poker_hand))
        hands.append(cards.ThreeOfAKind(poker_hand))
        hands.append(cards.TwoPairs(poker_hand))
        hands.append(cards.OnePair(poker_hand))
        hands.append(cards.HighCard(poker_hand))

        for hand in hands:
            if hand.is_match():
                return hand.get_rating()

    @staticmethod
    def score_hands(player_hands):
        scored = []
        for (player, hand) in player_hands:
            rating = Scorer.get_rating(hand)
            scored.append((player, hand, rating))

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
