
from cards import Card, FullHouse, Hand

class Test_FullHouse():

    def test_isMatch_fullHouse_1(self):
        hand = Hand([Card('2H'),Card('2S'),Card('2C'),Card('JH'),Card('JD')])
        fullHouse = FullHouse()
        assert fullHouse.is_match(hand) == True

    def test_isMatch_fullHouse_2(self):
        hand = Hand([Card('2H'),Card('2S'),Card('JC'),Card('JH'),Card('JD')])
        fullHouse = FullHouse()
        assert fullHouse.is_match(hand) == True

    def test_isMatch_notFourOfAKind(self):
        hand = Hand([Card('2H'),Card('2C'),Card('2D'),Card('2S'),Card('3D')])
        fullHouse = FullHouse()
        assert fullHouse.is_match(hand) == False

    def test_isMatch_notThreeOfAKind(self):
        hand = Hand([Card('2H'),Card('2C'),Card('2D'),Card('4S'),Card('3D')])
        fullHouse = FullHouse()
        assert fullHouse.is_match(hand) == False

    def test_isMatch_notTwoPairs(self):
        hand = Hand([Card('2H'),Card('2C'),Card('4D'),Card('4S'),Card('3D')])
        fullHouse = FullHouse()
        assert fullHouse.is_match(hand) == False

    def test_getRating_high(self):
        hand = Hand([Card('2S'),Card('2H'),Card('2D'),Card('JH'),Card('JS')])
        fullHouse = FullHouse()
        assert fullHouse.get_rating(hand) == (7, 2, 11, 99, 99, 99)

    def test_getRating_low(self):
        hand = Hand([Card('2S'),Card('2H'),Card('JD'),Card('JH'),Card('JS')])
        fullHouse = FullHouse()
        assert fullHouse.get_rating(hand) == (7, 11, 2, 99, 99, 99)
