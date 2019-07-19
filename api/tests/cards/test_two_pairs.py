import pytest
from cards import Card, Hand, TwoPairs

@pytest.mark.skip(reason='hardening') 
class Test_TwoPairs():

    def test_is_match_two_pairs(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('JH'),Card('JD')])
        two_pairs = TwoPairs(hand)
        assert two_pairs.is_match() == True

    def test_is_match_not_four_of_a_kind(self):
        hand = Hand([Card('2H'),Card('2S'),Card('2C'),Card('2D'),Card('JD')])
        two_pairs = TwoPairs(hand)
        assert two_pairs.is_match() == False

    def test_get_rating_1(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('JH'),Card('JS')])
        two_pairs = TwoPairs(hand)
        assert two_pairs.get_rating().get() == (3, 11, 2, 3, 99, 99, 'Two Pairs')

    def test_get_rating_2(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('3H'),Card('JS')])
        two_pairs = TwoPairs(hand)
        assert two_pairs.get_rating().get() == (3, 3, 2, 11, 99, 99, 'Two Pairs')

    def test_get_rating_partial(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3H'),Card('3S')])
        two_pairs = TwoPairs(hand)
        assert two_pairs.get_rating().get() == (3, 3, 2, 0, 99, 99, 'Two Pairs')
