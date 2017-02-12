
from cards import Card, Hand, OnePair

class Test_OnePair():

    def test_isMatch(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('4H'),Card('JD')])
        onePair = OnePair()
        assert onePair.IsMatch(hand) == True

    def test_isMatch_partial(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C')])
        onePair = OnePair()
        assert onePair.IsMatch(hand) == True

    def test_isMatch_only(self):
        hand = Hand([Card('2H'),Card('2S')])
        onePair = OnePair()
        assert onePair.IsMatch(hand) == True

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('4H'),Card('JS')])
        onePair = OnePair()
        assert onePair.GetRating(hand) == (2, 2, 11, 4, 3, 99)

    def test_getRating_partial(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D')])
        onePair = OnePair()
        assert onePair.GetRating(hand) == (2, 2, 3, 0, 0, 99)

    def test_getRating_only(self):
        hand = Hand([Card('2S'),Card('2H')])
        onePair = OnePair()
        assert onePair.GetRating(hand) == (2, 2, 0, 0, 0, 99)
