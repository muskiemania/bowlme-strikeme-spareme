
from cards import Card, FullHouse, Hand

class Test_FullHouse():

    def test_is_match_full_house_1(self):
        hand = Hand([Card('2H'),Card('2S'),Card('2C'),Card('JH'),Card('JD')])
        full_house = FullHouse(hand)
        assert full_house.is_match() == True

    def test_is_match_full_house_2(self):
        hand = Hand([Card('2H'),Card('2S'),Card('JC'),Card('JH'),Card('JD')])
        full_house = FullHouse(hand)
        assert full_house.is_match() == True

    def test_isMatch_not_four_of_a_kind(self):
        hand = Hand([Card('2H'),Card('2C'),Card('2D'),Card('2S'),Card('3D')])
        full_house = FullHouse(hand)
        assert full_house.is_match() == False

    def test_isMatch_not_three_of_a_kind(self):
        hand = Hand([Card('2H'),Card('2C'),Card('2D'),Card('4S'),Card('3D')])
        full_house = FullHouse(hand)
        assert full_house.is_match() == False

    def test_isMatch_not_two_pairs(self):
        hand = Hand([Card('2H'),Card('2C'),Card('4D'),Card('4S'),Card('3D')])
        full_house = FullHouse(hand)
        assert full_house.is_match() == False

    def test_get_rating_high(self):
        hand = Hand([Card('2S'),Card('2H'),Card('2D'),Card('JH'),Card('JS')])
        full_house = FullHouse(hand)
        assert full_house.get_rating().get() == (7, 2, 11, 99, 99, 99, 'Full House')

    def test_get_rating_low(self):
        hand = Hand([Card('2S'),Card('2H'),Card('JD'),Card('JH'),Card('JS')])
        full_house = FullHouse(hand)
        assert full_house.get_rating().get() == (7, 11, 2, 99, 99, 99, 'Full House')
