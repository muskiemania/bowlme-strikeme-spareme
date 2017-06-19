import pytest
from cards import Card, Hand
from scoring import Scorer

class Test_Scorer:
    def test_getRating_royalFlush(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer().get_rating(hand)
        assert rating == (10, 14,13,12,11,10)

    def test_getRating_straightFlush(self):
        hand = Hand([Card('9H'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer().get_rating(hand)
        assert rating == (9, 13,12,11,10,9)

    def test_getRating_fourOfAKind(self):
        hand = Hand([Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('TH')])
        rating = Scorer().get_rating(hand)
        assert rating == (8, 13,10,99,99,99)

    def test_getRating_fullHouse(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('QD'), Card('QC')])
        rating = Scorer().get_rating(hand)
        assert rating == (7, 12,14,99,99,99)

    def test_getRating_flush(self):
        hand = Hand([Card('AH'), Card('9H'), Card('QH'), Card('JH'), Card('4H')])
        rating = Scorer().get_rating(hand)
        assert rating == (6, 14,12,11,9,4)

    def test_getRating_straight(self):
        hand = Hand([Card('9H'), Card('KS'), Card('QD'), Card('JH'), Card('TC')])
        rating = Scorer().get_rating(hand)
        assert rating == (5, 13,12,11,10,9)

    def test_getRating_threeOfAKind(self):
        hand = Hand([Card('AH'), Card('KH'), Card('KD'), Card('KC'), Card('TH')])
        rating = Scorer().get_rating(hand)
        assert rating == (4, 13,14,10,99,99)

    def test_getRating_twoPairs(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer().get_rating(hand)
        assert rating == (3, 14,11,12,99,99)

    def test_getRating_onePair(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer().get_rating(hand)
        assert rating == (2, 11,14,13,12,99)

    def test_getRating_highCard(self):
        hand = Hand([Card('AH'), Card('QS'), Card('JD'), Card('9H'), Card('4H')])
        rating = Scorer().get_rating(hand)
        assert rating == (1, 14,12,11,9,4)

    def test_scoreHands(self):
        royal = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        straight_flush = Hand([Card('9H'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        four_of_kind = Hand([Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('TH')])
        full_house = Hand([Card('AH'), Card('AS'), Card('QH'), Card('QD'), Card('QC')])
        flush = Hand([Card('AH'), Card('9H'), Card('QH'), Card('JH'), Card('4H')])
        straight = Hand([Card('9H'), Card('KS'), Card('QD'), Card('JH'), Card('TC')])
        three_of_kind = Hand([Card('AH'), Card('KH'), Card('KD'), Card('KC'), Card('TH')])
        two_pairs = Hand([Card('AH'), Card('AS'), Card('QH'), Card('JH'), Card('JS')])
        one_pair = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('JS')])
        high_card = Hand([Card('AH'), Card('QS'), Card('JD'), Card('9H'), Card('4H')])

        player_hands = []
        player_hands.append(('royal', royal))
        player_hands.append(('straight_flush', straight_flush))
        player_hands.append(('four_of_kind', four_of_kind))
        player_hands.append(('full_house', full_house))
        player_hands.append(('flush', flush))
        player_hands.append(('straight', straight))
        player_hands.append(('three_of_kind', three_of_kind))
        player_hands.append(('two_pairs', two_pairs))
        player_hands.append(('one_pair', one_pair))
        player_hands.append(('high_card', high_card))

        scored_hands = Scorer().score_hands(player_hands)
        for (player, hand, rating) in scored_hands:
            assert rating == Scorer().get_rating(hand)

            
    def test_rankHands_1(self):
        scored = []
        scored.append(('justin', None, (3,14,19,13,99,99)))
        scored.append(('sarah', None, (2,13,11,10,4,99)))

        ranked = Scorer().rank_hands(scored)

        for index in range(0, 2):
            (player, hand, score, rank) = ranked[index]
            assert rank == index+1

    def test_rankHands_2(self):
        scored = []
        scored.append(('justin', None, (2,13,11,10,4,99)))
        scored.append(('sarah', None, (2,13,11,10,4,99)))

        ranked = Scorer().rank_hands(scored)

        for (player, hand, score, rank) in ranked:
            assert rank == 1

    def test_rankHands_3(self):
        scored = []
        scored.append(('justin', None, (1,13,11,10,4,2)))
        scored.append(('sarah', None, (1,13,11,10,4,2)))
        scored.append(('jenna', None, (1,13,11,10,4,2)))

        ranked = Scorer().rank_hands(scored)

        for (player, hand, score, rank) in ranked:
            assert rank == 1

    def test_rankHands_4(self):
        scored = []
        scored.append(('justin', None, (2,13,11,10,4,99)))
        scored.append(('sarah', None, (1,13,11,10,4,2)))
        scored.append(('jenna', None, (1,13,11,10,4,2)))

        ranked = Scorer().rank_hands(scored)[-2:]

        for (player, hand, score, rank) in ranked:
            assert rank == 2
