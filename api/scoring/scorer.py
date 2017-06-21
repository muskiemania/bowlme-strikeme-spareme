import cards

class Scorer:

    def __init__(self):
        pass

    @staticmethod
    def get_rating(hand):
        hands = []
        hands.append(cards.StraightFlush(hand))
        hands.append(cards.FourOfAKind(hand))
        hands.append(cards.FullHouse(hand))
        hands.append(cards.Flush(hand))
        hands.append(cards.Straight(hand))
        hands.append(cards.ThreeOfAKind(hand))
        hands.append(cards.TwoPairs(hand))
        hands.append(cards.OnePair(hand))
        hands.append(cards.HighCard(hand))

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
        for i in range(5, -1, -1):
            player_hands.sort(key=lambda (p, h, r): r[i], reverse=True)

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

    @staticmethod
    def get_leaderboard(player_hands):
        scored_hands = Scorer.score_hands(player_hands)
        return Scorer.rank_hands(player_hands)
