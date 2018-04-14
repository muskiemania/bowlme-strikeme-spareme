
from cards import Card, Hand, ThreeOfAKind

class Test_ThreeOfAKind():

    def test_is_match_three_of_a_kind(self):
        hand = Hand([Card('2H'),Card('2S'),Card('3C'),Card('JH'),Card('2D')])
        three_of_a_kind = ThreeOfAKind(hand)
        assert three_of_a_kind.is_match() == True

    def test_get_rating(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('JH'),Card('2C')])
        three_of_a_kind = ThreeOfAKind(hand)
        assert three_of_a_kind.get_rating().get() == (4, 2, 11, 3, 99, 99, 'Three-Of-A-Kind')

    def test_get_rating_full_house(self):
        hand = Hand([Card('2S'),Card('2H'),Card('3D'),Card('3H'),Card('3S')])
        three_of_a_kind = ThreeOfAKind(hand)
        assert three_of_a_kind.get_rating().get() == (4, 3, 2, 99, 99, 99, 'Three-Of-A-Kind')

    def test_get_rating_partial_1(self):
        hand = Hand([Card('2S'),Card('2H'),Card('JH'),Card('2C')])
        three_of_a_kind = ThreeOfAKind(hand)
        assert three_of_a_kind.get_rating().get() == (4, 2, 11, 0, 99, 99, 'Three-Of-A-Kind')

    def test_get_rating_partial_2(self):
        hand = Hand([Card('2S'),Card('2H'),Card('2C')])
        three_of_a_kind = ThreeOfAKind(hand)
        assert three_of_a_kind.get_rating().get() == (4, 2, 0, 0, 99, 99, 'Three-Of-A-Kind')
