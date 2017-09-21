import pytest
from cards import Card, Hand
from scoring import Scorer

class Test_Scorer:
    def test_get_rating_royal_flush(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer(hand).get_rating()
        assert rating == (10, 14, 13, 12, 11, 10)

    def test_get_rating_straight_flush(self):
        hand = Hand([Card('9H'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer(hand).get_rating()
        assert rating == (9, 13, 12, 11, 10, 9)

    def test_get_rating_four_of_a_kind(self):
        hand = Hand([Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('TH')])
        rating = Scorer(hand).get_rating()
        assert rating == (8, 13, 10, 99, 99, 99)

    def test_get_rating_full_house(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('QD'), Card('QC')])
        rating = Scorer(hand).get_rating()
        assert rating == (7, 12, 14, 99, 99, 99)

    def test_get_rating_flush(self):
        hand = Hand([Card('AH'), Card('9H'), Card('QH'), Card('JH'), Card('4H')])
        rating = Scorer(hand).get_rating()
        assert rating == (6, 14, 12, 11, 9, 4)

    def test_get_rating_straight(self):
        hand = Hand([Card('9H'), Card('KS'), Card('QD'), Card('JH'), Card('TC')])
        rating = Scorer(hand).get_rating()
        assert rating == (5, 13, 12, 11, 10, 9)

    def test_get_rating_three_of_a_kind(self):
        hand = Hand([Card('AH'), Card('KH'), Card('KD'), Card('KC'), Card('TH')])
        rating = Scorer(hand).get_rating()
        assert rating == (4, 13, 14, 10, 99, 99)

    def test_get_rating_two_pairs(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer(hand).get_rating()
        assert rating == (3, 14, 11, 12, 99, 99)

    def test_get_rating_one_pair(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer(hand).get_rating()
        assert rating == (2, 11, 14, 13, 12, 99)

    def test_get_rating_high_card(self):
        hand = Hand([Card('AH'), Card('QS'), Card('JD'), Card('9H'), Card('4H')])
        rating = Scorer(hand).get_rating()
        assert rating == (1, 14, 12, 11, 9, 4)

    def test_score_hands(self):
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

        scored_hands = Scorer.score_hands(player_hands)
        for (_, hand, rating) in scored_hands:
            assert rating == Scorer.get_rating(hand)

            
    def test_rank_hands_1(self):
        scored = []
        scored.append(('justin', None, (3,14,19,13,99,99)))
        scored.append(('sarah', None, (2,13,11,10,4,99)))

        ranked = Scorer.rank_hands(scored)

        for index in range(0, 2):
            (player, hand, score, rank) = ranked[index]
            assert rank == index+1

    def test_rank_hands_2(self):
        scored = []
        scored.append(('justin', None, (2,13,11,10,4,99)))
        scored.append(('sarah', None, (2,13,11,10,4,99)))

        ranked = Scorer.rank_hands(scored)

        for (player, hand, score, rank) in ranked:
            assert rank == 1

    def test_rank_hands_3(self):
        scored = []
        scored.append(('justin', None, (1,13,11,10,4,2)))
        scored.append(('sarah', None, (1,13,11,10,4,2)))
        scored.append(('jenna', None, (1,13,11,10,4,2)))

        ranked = Scorer.rank_hands(scored)

        for (player, hand, score, rank) in ranked:
            assert rank == 1

    def test_rank_hands_4(self):
        scored = []
        scored.append(('justin', None, (2,13,11,10,4,99)))
        scored.append(('sarah', None, (1,13,11,10,4,2)))
        scored.append(('jenna', None, (1,13,11,10,4,2)))

        ranked = Scorer.rank_hands(scored)[-2:]

        for (player, hand, score, rank) in ranked:
            assert rank == 2
