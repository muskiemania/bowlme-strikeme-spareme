
from cards import Card, Hand, Straight

class Test_Straight():
 
    def test_isMatch_1(self):
        hand = Hand([Card('2H'),Card('3S'),Card('6C'),Card('5H'),Card('4D')])
        straight = Straight()
        assert straight.is_match(hand) == True

    def test_isMatch_2(self):
        hand = Hand([Card('9H'),Card('KH'),Card('QH'),Card('JH'),Card('TH')])
        straight = Straight()
        assert straight.is_match(hand) == True

    def test_isMatch_notEnoughCards(self):
        hand = Hand([Card('3H'),Card('6C'),Card('5H'),Card('4D')])
        straight = Straight()
        assert straight.is_match(hand) == False

    def test_isMatch_aceHigh(self):
        hand = Hand([Card('TH'),Card('JS'),Card('KC'),Card('AD'),Card('QD')])
        straight = Straight()
        assert straight.is_match(hand) == True

    def test_isMatch_aceLow(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_match(hand) == True

    def test_isCoherent_1(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_coherent(hand) == True
        
    def test_isCoherent_2(self):
        hand = Hand([Card('KH'),Card('AS'),Card('JC'),Card('TD'),Card('QD')])
        straight = Straight()
        assert straight.is_coherent(hand) == True
        
    def test_isCoherent_3(self):
        hand = Hand([Card('5H'),Card('6S'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_coherent(hand) == True
        
    def test_isCoherent_4(self):
        hand = Hand([Card('5H'),Card('6S'),Card('6C'),Card('3D'),Card('4D')])
        straight = Straight()
        assert straight.is_coherent(hand) == True
        
    def test_isCoherent_5(self):
        hand = Hand([Card('5H'),Card('AS'),Card('KC'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_coherent(hand) == False

    def test_isCoherent_6(self):
        hand = Hand([Card('5H'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_coherent(hand) == True

    def test_isCoherent_7(self):
        hand = Hand([Card('5H'),Card('AS'),Card('KC'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_coherent(hand) == False
    
    def test_isLowStraight_1(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight()
        assert straight.is_low_straight(hand) == True

    def test_isLowStraight_2(self):
        hand = Hand([Card('5H'),Card('2S'),Card('6C'),Card('3D'),Card('4D')])
        straight = Straight()
        assert straight.is_low_straight(hand) == False

    def test_isLowStraight_3(self):
        hand = Hand([Card('AH'),Card('TS'),Card('JC'),Card('KD'),Card('QD')])
        straight = Straight()
        assert straight.is_low_straight(hand) == False

    def test_getRating(self):
        hand = Hand([Card('4S'),Card('5H'),Card('8D'),Card('7H'),Card('6S')])
        straight = Straight()
        assert straight.get_rating(hand) == (5, 8, 7, 6, 5, 4)

    def test_getRating_aceHigh(self):
        hand = Hand([Card('AS'),Card('TH'),Card('QD'),Card('JH'),Card('KS')])
        straight = Straight()
        assert straight.get_rating(hand) == (5, 14, 13, 12, 11, 10)

    def test_getRating_aceLow(self):
        hand = Hand([Card('2S'),Card('AH'),Card('3D'),Card('5H'),Card('4S')])
        straight = Straight()
        assert straight.get_rating(hand) == (5, 5, 4, 3, 2, 1)
