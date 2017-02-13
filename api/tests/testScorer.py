import pytest
from cards import Card, Hand
from scoring import Scorer

class Test_Scorer:
    def test_getRating_royalFlush(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer().GetRating(hand)
        assert rating == (10, 14,13,12,11,10)

    def test_getRating_straightFlush(self):
        hand = Hand([Card('9H'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer().GetRating(hand)
        assert rating == (9, 13,12,11,10,9)

    def test_getRating_fourOfAKind(self):
        hand = Hand([Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('TH')])
        rating = Scorer().GetRating(hand)
        assert rating == (8, 13,10,99,99,99)

    def test_getRating_fullHouse(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('QD'), Card('QC')])
        rating = Scorer().GetRating(hand)
        assert rating == (7, 12,14,99,99,99)

    def test_getRating_flush(self):
        hand = Hand([Card('AH'), Card('9H'), Card('QH'), Card('JH'), Card('4H')])
        rating = Scorer().GetRating(hand)
        assert rating == (6, 14,12,11,9,4)

    def test_getRating_straight(self):
        hand = Hand([Card('9H'), Card('KS'), Card('QD'), Card('JH'), Card('TC')])
        rating = Scorer().GetRating(hand)
        assert rating == (5, 13,12,11,10,9)

    def test_getRating_threeOfAKind(self):
        hand = Hand([Card('AH'), Card('KH'), Card('KD'), Card('KC'), Card('TH')])
        rating = Scorer().GetRating(hand)
        assert rating == (4, 13,14,10,99,99)

    def test_getRating_twoPairs(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer().GetRating(hand)
        assert rating == (3, 14,11,12,99,99)

    def test_getRating_onePair(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer().GetRating(hand)
        assert rating == (2, 11,14,13,12,99)

    def test_getRating_highCard(self):
        hand = Hand([Card('AH'), Card('QS'), Card('JD'), Card('9H'), Card('4H')])
        rating = Scorer().GetRating(hand)
        assert rating == (1, 14,12,11,9,4)

    def test_scoreHands(self):
        royal = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        straightFlush = Hand([Card('9H'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        fourOfKind = Hand([Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('TH')])
        fullHouse = Hand([Card('AH'), Card('AS'), Card('QH'), Card('QD'), Card('QC')])
        flush = Hand([Card('AH'), Card('9H'), Card('QH'), Card('JH'), Card('4H')])
        straight = Hand([Card('9H'), Card('KS'), Card('QD'), Card('JH'), Card('TC')])
        threeOfKind = Hand([Card('AH'), Card('KH'), Card('KD'), Card('KC'), Card('TH')])
        twoPairs = Hand([Card('AH'), Card('AS'), Card('QH'), Card('JH'), Card('JS')])
        onePair = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('JS')])
        highCard = Hand([Card('AH'), Card('QS'), Card('JD'), Card('9H'), Card('4H')])

        playerHands = []
        playerHands.append(('royal', royal))
        playerHands.append(('straightFlush', straightFlush))
        playerHands.append(('fourOfKind', fourOfKind))
        playerHands.append(('fullHouse', fullHouse))
        playerHands.append(('flush', flush))
        playerHands.append(('straight', straight))
        playerHands.append(('threeOfKind', threeOfKind))
        playerHands.append(('twoPairs', twoPairs))
        playerHands.append(('onePair', onePair))
        playerHands.append(('highCard', highCard))

        scoredHands = Scorer().ScoreHands(playerHands)
        for (player, hand, rating) in scoredHands:
            assert rating == Scorer().GetRating(hand)

            
    def test_rankHands_1(self):
        scored = []
        scored.append(('justin', None, (3,14,19,13,99,99)))
        scored.append(('sarah', None, (2,13,11,10,4,99)))

        ranked = Scorer().RankHands(scored)

        for index in range(0, 2):
            (player, hand, score, rank) = ranked[index]
            assert rank == index+1

    def test_rankHands_2(self):
        scored = []
        scored.append(('justin', None, (2,13,11,10,4,99)))
        scored.append(('sarah', None, (2,13,11,10,4,99)))

        ranked = Scorer().RankHands(scored)

        for (player, hand, score, rank) in ranked:
            assert rank == 1

    def test_rankHands_3(self):
        scored = []
        scored.append(('justin', None, (1,13,11,10,4,2)))
        scored.append(('sarah', None, (1,13,11,10,4,2)))
        scored.append(('jenna', None, (1,13,11,10,4,2)))

        ranked = Scorer().RankHands(scored)

        for (player, hand, score, rank) in ranked:
            assert rank == 1

    def test_rankHands_4(self):
        scored = []
        scored.append(('justin', None, (2,13,11,10,4,99)))
        scored.append(('sarah', None, (1,13,11,10,4,2)))
        scored.append(('jenna', None, (1,13,11,10,4,2)))

        ranked = Scorer().RankHands(scored)[-2:]

        for (player, hand, score, rank) in ranked:
            assert rank == 2
