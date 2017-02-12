
from cards import Card, Hand, Straight

class Test_Straight():
 
    def test_isMatch(self):
        hand = Hand([Card('2H'),Card('3S'),Card('6C'),Card('5H'),Card('4D')])
        straight = Straight()
        assert straight.IsMatch(hand) == True

    def test_isMatch_notEnoughCards(self):
        hand = Hand([Card('3H'),Card('6C'),Card('5H'),Card('4D')])
        straight = Straight()
        assert straight.IsMatch(hand) == False

    def test_isMatch_aceHigh(self):
        hand = Hand([Card('TH'),Card('JS'),Card('KC'),Card('AD'),Card('QD')])
        straight = Straight()
        assert straight.IsMatch(hand) == True

    def test_isMatch_aceLow(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.IsMatch(hand) == True

    def test_isMatch_notAStraight(self):
        hand = Hand([Card('TH'),Card('4S'),Card('7C'),Card('AD'),Card('QD')])
        straight = Straight()
        assert straight.IsMatch(hand) == False

    def test_getRating(self):
        hand = Hand([Card('4S'),Card('5H'),Card('8D'),Card('7H'),Card('6S')])
        straight = Straight()
        assert straight.GetRating(hand) == (5, 8, 7, 6, 5, 4)

    def test_getRating_aceHigh(self):
        hand = Hand([Card('AS'),Card('TH'),Card('QD'),Card('JH'),Card('KS')])
        straight = Straight()
        assert straight.GetRating(hand) == (5, 14, 13, 12, 11, 10)

    def test_getRating_aceLow(self):
        hand = Hand([Card('2S'),Card('AH'),Card('3D'),Card('5H'),Card('4S')])
        straight = Straight()
        assert straight.GetRating(hand) == (5, 5, 4, 3, 2, 1)
