
from cards import Card, Hand, ThreeOfAKind

class Test_ThreeOfAKind():

    def test_isMatch_threeOfAKind(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('JH'),Card('2D')])
        threeOfAKind = ThreeOfAKind()
        threeOfAKind.IsMatch(hand) == True

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('JH'),Card('2C')])
        threeOfAKind = ThreeOfAKind()
        assert threeOfAKind.GetRating(hand) == (4, 2, 11, 3, 99, 99)

    def test_getRating_fullHouse(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('3H'),Card('3S')])
        threeOfAKind = ThreeOfAKind()
        assert threeOfAKind.GetRating(hand) == (4, 3, 2, 99, 99, 99)

    def test_getRating_partial_1(self):
        hand = Hand([Card('2S'),Card('2H'),Card('JH'),Card('2C')])
        threeOfAKind = ThreeOfAKind()
        assert threeOfAKind.GetRating(hand) == (4, 2, 11, 0, 99, 99)

    def test_getRating_partial_2(self):
        hand = Hand([Card('2S'),Card('2H'),Card('2C')])
        threeOfAKind = ThreeOfAKind()
        assert threeOfAKind.GetRating(hand) == (4, 2, 0, 0, 99, 99)
