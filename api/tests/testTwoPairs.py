
from cards import Card, Hand, TwoPairs

class Test_TwoPairs():

    def test_isMatch_twoPairs(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('JH'),Card('JD')])
        two_pairs = TwoPairs()
        assert two_pairs.is_match(hand) == True

    def test_isMatch_notFourOfAKind(self):
        hand = Hand([Card('2H'),Card('2S'),Card('2C'),Card('2D'),Card('JD')])
        two_pairs = TwoPairs()
        assert two_pairs.is_match(hand) == False

    def test_getRating_1(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('JH'),Card('JS')])
        two_pairs = TwoPairs()
        assert two_pairs.get_rating(hand) == (3, 11, 2, 3, 99, 99)

    def test_getRating_2(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('3H'),Card('JS')])
        two_pairs = TwoPairs()
        assert two_pairs.get_rating(hand) == (3, 3, 2, 11, 99, 99)

    def test_getRating_partial(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3H'),Card('3S')])
        two_pairs = TwoPairs()
        assert two_pairs.get_rating(hand) == (3, 3, 2, 0, 99, 99)
