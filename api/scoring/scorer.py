import cards

class Scorer:

    def __init__(self):
        pass

    def GetRating(self, hand):
        hands = [cards.StraightFlush(), cards.FourOfAKind(), cards.FullHouse(), cards.Flush(), cards.Straight(), cards.ThreeOfAKind(), cards.TwoPairs(), cards.OnePair(), cards.HighCard()]

        for h in hands:
            if h.IsMatch(hand):
                print h
                return h.GetRating(hand)

    def ScoreHands(self, playerHands):
        scored = []
        for (player, hand) in playerHands:
            rating = Scorer().GetRating(hand)
            scored.append((player, hand, rating))

        return scored

    def RankHands(self, playerHands):
        for i in range(5, -1, -1):
            playerHands.sort(key=lambda (p, h, r): r[i], reverse=True)

        ranked = []
        index = 0
        currentRank = 1
        
        for (player, hand, score) in playerHands:
            if index == 0:
                ranked.append((player, hand, score, currentRank))
                index += 1
            else:             
                if score != ranked[index - 1][3]:
                    currentRank += 1

                ranked.append((player, hand, score, currentRank))
                index += 1

        return ranked

    @staticmethod
    def GetLeaderboard(playerHands):
        scoredHands = Scorer().ScoreHands(playerHands)
        return Scorer().RankHands(playerHands)
