
from cards import Card, Hand, OnePair

class Test_OnePair():

    def test_is_match(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('4H'),Card('JD')])
        one_pair = OnePair(hand)
        assert one_pair.is_match() == True

    def test_is_match_partial(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C')])
        one_pair = OnePair(hand)
        assert one_pair.is_match() == True

    def test_is_match_only(self):
        hand = Hand([Card('2H'),Card('2S')])
        one_pair = OnePair(hand)
        assert one_pair.is_match() == True

    def test_get_rating(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('4H'),Card('JS')])
        one_pair = OnePair(hand)
        assert one_pair.get_rating() == (2, 2, 11, 4, 3, 99)

    def test_get_rating_partial(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D')])
        one_pair = OnePair(hand)
        assert one_pair.get_rating() == (2, 2, 3, 0, 0, 99)

    def test_get_rating_only(self):
        hand = Hand([Card('2S'),Card('2H')])
        one_pair = OnePair(hand)
        assert one_pair.get_rating() == (2, 2, 0, 0, 0, 99)
