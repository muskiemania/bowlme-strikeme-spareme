import pytest
from cards import Card, Hand, PokerHand
from bowl_redis_dto import RatingDto
from scoring import Scorer

class Test_Scorer:
    def test_get_rating_royal_flush(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (10, 14, 13, 12, 11, 10, 'Royal Flush')

    def test_get_rating_straight_flush(self):
        hand = Hand([Card('9H'), Card('KH'), Card('QH'), Card('JH'), Card('TH')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (9, 13, 12, 11, 10, 9, 'Straight Flush')

    def test_get_rating_four_of_a_kind(self):
        hand = Hand([Card('KH'), Card('KD'), Card('KC'), Card('KS'), Card('TH')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (8, 13, 10, 99, 99, 99, 'Four-Of-A-Kind')

    def test_get_rating_full_house(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('QD'), Card('QC')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (7, 12, 14, 99, 99, 99, 'Full House')

    def test_get_rating_flush(self):
        hand = Hand([Card('AH'), Card('9H'), Card('QH'), Card('JH'), Card('4H')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (6, 14, 12, 11, 9, 4, 'Flush')

    def test_get_rating_straight(self):
        hand = Hand([Card('9H'), Card('KS'), Card('QD'), Card('JH'), Card('TC')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (5, 13, 12, 11, 10, 9, 'Straight')

    def test_get_rating_three_of_a_kind(self):
        hand = Hand([Card('AH'), Card('KH'), Card('KD'), Card('KC'), Card('TH')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (4, 13, 14, 10, 99, 99, 'Three-Of-A-Kind')

    def test_get_rating_two_pairs(self):
        hand = Hand([Card('AH'), Card('AS'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (3, 14, 11, 12, 99, 99, 'Two Pairs')

    def test_get_rating_one_pair(self):
        hand = Hand([Card('AH'), Card('KH'), Card('QH'), Card('JH'), Card('JS')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (2, 11, 14, 13, 12, 99, 'One Pair')

    def test_get_rating_high_card(self):
        hand = Hand([Card('AH'), Card('QS'), Card('JD'), Card('9H'), Card('4H')])
        rating = Scorer(hand).get_rating().get()
        assert rating == (1, 14, 12, 11, 9, 4, 'High Card')

    def test_rank_hands_1(self):

        justin = RatingDto((3, 14, 19, 13, 99, 99, ''), 'justin')
        justin.rank = 12

        sarah = RatingDto((2, 13, 11, 10, 4, 99, ''), 'sarah')
        sarah.rank = 13

        ranked = Scorer.rank_hands([justin, sarah])

        assert ranked[0].player_id == 'justin' and ranked[0].rank == 1
        assert ranked[1].player_id == 'sarah' and ranked[1].rank == 2

    def test_rank_hands_2(self):

        justin = RatingDto((2, 13, 11, 10, 4, 99, ''), 'justin')
        sarah = RatingDto((2, 13, 11, 10, 4, 99, ''), 'sarah')

        ranked = Scorer.rank_hands([justin, sarah])

        assert ranked[0].rank == 1
        assert ranked[1].rank == 1

    def test_rank_hands_3(self):

        justin = RatingDto((1, 13, 11, 10, 4, 2), 'justin')
        sarah = RatingDto((1, 13, 11, 10, 4, 2), 'sarah')
        jenna = RatingDto((1, 13, 11, 10, 4, 2), 'jenna')

        ranked = Scorer.rank_hands([jenna, justin, sarah])

        assert ranked[0].rank == 1
        assert ranked[1].rank == 1
        assert ranked[2].rank == 1

    def test_rank_hands_4(self):

        justin = RatingDto((2, 13, 11, 10, 4, 99, ''), 'justin')
        sarah = RatingDto((1, 13, 11, 10, 4, 2, ''), 'sarah')
        jenna = RatingDto((1, 13, 11, 10, 4, 2, ''), 'jenna')

        ranked = Scorer.rank_hands([justin, jenna, sarah])

        assert ranked[0].rank == 1 and ranked[0].player_id == 'justin'
        assert ranked[1].rank == 2
        assert ranked[2].rank == 2

    def test_rank_hands_5(self):

        justin = RatingDto((2, 13, 11, 10, 4, 99, ''), 'justin')
        sarah = RatingDto((1, 13, 11, 10, 4, 2, ''), 'sarah')
        jenna = RatingDto((1, 13, 11, 10, 4, 2, ''), 'jenna')
        paige = RatingDto((0, 0, 0, 0, 0, 0, ''), 'paige')

        ranked = Scorer.rank_hands([justin, jenna, sarah, paige])

        assert ranked[0].rank == 1 and ranked[0].player_id == 'justin'
        assert ranked[1].rank == 2
        assert ranked[2].rank == 2
        assert ranked[3].rank == 4 and ranked[3].player_id == 'paige'
