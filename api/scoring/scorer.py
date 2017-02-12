import cards

class Scorer:

    @staticmethod
    def GetRating(hand):
        hands = [cards.StraightFlush(), cards.FourOfAKind(), cards.FullHouse(), cards.Flush(), cards.Straight(), cards.ThreeOfAKind(), cards.TwoPairs(), cards.OnePair(), cards.HighCard()]

        for h in hands:
            if h.IsMatch(hand):
                return h.GetRating(hand)
    
    @staticmethod
    def ScoreHands(playerHands):

        scored = []
        for (player, hand) in playerHands:
            rating = Scorer.GetRating(hand)
            scored.append((player, hand, rating))

        for i in range(5, -1, -1):
            print i
            sorted(scored, key=lambda (p, h, r): r[i], reverse=True)

        ranked = []
        index = 0
        currentRank = 1
        
        for (player, hand, score) in scored:
            if index == 0:
                ranked.append((player, hand, score, currentRank))
                index += 1
            else:             
                if score != ranked[index - 1][3]:
                    currentRank += 1

                ranked.append((player, hand, score, currentRank))
                index += 1

        print ranked
        return ranked
