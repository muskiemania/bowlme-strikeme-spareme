import cards

class Scorer:

    def __init__(self):
        pass

    def get_rating(self, hand):
        hands = [cards.StraightFlush(), cards.FourOfAKind(), cards.FullHouse(), cards.Flush(), cards.Straight(), cards.ThreeOfAKind(), cards.TwoPairs(), cards.OnePair(), cards.HighCard()]

        for h in hands:
            if h.is_match(hand):
                print h
                return h.get_rating(hand)

    def score_hands(self, player_hands):
        scored = []
        for (player, hand) in player_hands:
            rating = Scorer().get_rating(hand)
            scored.append((player, hand, rating))

        return scored

    def rank_hands(self, player_hands):
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
        scored_hands = Scorer().score_hands(player_hands)
        return Scorer().rank_hands(player_hands)
