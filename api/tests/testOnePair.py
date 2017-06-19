
from cards import Card, Hand, OnePair

class Test_OnePair():

    def test_isMatch(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('4H'),Card('JD')])
        one_pair = OnePair()
        assert one_pair.is_match(hand) == True

    def test_isMatch_partial(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C')])
        one_pair = OnePair()
        assert one_pair.is_match(hand) == True

    def test_isMatch_only(self):
        hand = Hand([Card('2H'),Card('2S')])
        one_pair = OnePair()
        assert one_pair.is_match(hand) == True

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('4H'),Card('JS')])
        one_pair = OnePair()
        assert one_pair.get_rating(hand) == (2, 2, 11, 4, 3, 99)

    def test_getRating_partial(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D')])
        one_pair = OnePair()
        assert one_pair.get_rating(hand) == (2, 2, 3, 0, 0, 99)

    def test_getRating_only(self):
        hand = Hand([Card('2S'),Card('2H')])
        one_pair = OnePair()
        assert one_pair.get_rating(hand) == (2, 2, 0, 0, 0, 99)
