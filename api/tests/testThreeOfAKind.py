
from cards import Card, Hand, ThreeOfAKind

class Test_ThreeOfAKind():

    def test_isMatch_threeOfAKind(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('JH'),Card('2D')])
        three_of_a_kind = ThreeOfAKind()
        assert three_of_a_kind.is_match(hand) == True

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('JH'),Card('2C')])
        three_of_a_kind = ThreeOfAKind()
        assert three_of_a_kind.get_rating(hand) == (4, 2, 11, 3, 99, 99)

    def test_getRating_fullHouse(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('3H'),Card('3S')])
        three_of_a_kind = ThreeOfAKind()
        assert three_of_a_kind.get_rating(hand) == (4, 3, 2, 99, 99, 99)

    def test_getRating_partial_1(self):
        hand = Hand([Card('2S'),Card('2H'),Card('JH'),Card('2C')])
        three_of_a_kind = ThreeOfAKind()
        assert three_of_a_kind.get_rating(hand) == (4, 2, 11, 0, 99, 99)

    def test_getRating_partial_2(self):
        hand = Hand([Card('2S'),Card('2H'),Card('2C')])
        three_of_a_kind = ThreeOfAKind()
        assert three_of_a_kind.get_rating(hand) == (4, 2, 0, 0, 99, 99)
