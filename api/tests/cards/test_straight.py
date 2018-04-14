
from cards import Card, Hand, Straight

class Test_Straight():
 
    def test_is_match_1(self):
        hand = Hand([Card('2H'),Card('3S'),Card('6C'),Card('5H'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_match() == True

    def test_is_match_2(self):
        hand = Hand([Card('9H'),Card('KH'),Card('QH'),Card('JH'),Card('TH')])
        straight = Straight(hand)
        assert straight.is_match() == True

    def test_is_match_not_enough_cards(self):
        hand = Hand([Card('3H'),Card('6C'),Card('5H'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_match() == False

    def test_is_match_ace_high(self):
        hand = Hand([Card('TH'),Card('JS'),Card('KC'),Card('AD'),Card('QD')])
        straight = Straight(hand)
        assert straight.is_match() == True

    def test_is_match_ace_low(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_match() == True

    def test_is_coherent_1(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_coherent() == True
        
    def test_is_coherent_2(self):
        hand = Hand([Card('KH'),Card('AS'),Card('JC'),Card('TD'),Card('QD')])
        straight = Straight(hand)
        assert straight.is_coherent() == True
        
    def test_is_coherent_3(self):
        hand = Hand([Card('5H'),Card('6S'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_coherent() == True
        
    def test_is_coherent_4(self):
        hand = Hand([Card('5H'),Card('6S'),Card('6C'),Card('3D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_coherent() == True
        
    def test_is_coherent_5(self):
        hand = Hand([Card('5H'),Card('AS'),Card('KC'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_coherent() == False

    def test_is_coherent_6(self):
        hand = Hand([Card('5H'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_coherent() == True

    def test_is_coherent_7(self):
        hand = Hand([Card('5H'),Card('AS'),Card('KC'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_coherent() == False
    
    def test_is_low_straight_1(self):
        hand = Hand([Card('5H'),Card('AS'),Card('3C'),Card('2D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_low_straight() == True

    def test_is_low_straight_2(self):
        hand = Hand([Card('5H'),Card('2S'),Card('6C'),Card('3D'),Card('4D')])
        straight = Straight(hand)
        assert straight.is_low_straight() == False

    def test_is_low_straight_3(self):
        hand = Hand([Card('AH'),Card('TS'),Card('JC'),Card('KD'),Card('QD')])
        straight = Straight(hand)
        assert straight.is_low_straight() == False

    def test_get_rating(self):
        hand = Hand([Card('4S'),Card('5H'),Card('8D'),Card('7H'),Card('6S')])
        straight = Straight(hand)
        assert straight.get_rating().get() == (5, 8, 7, 6, 5, 4, 'Straight')

    def test_get_rating_ace_high(self):
        hand = Hand([Card('AS'),Card('TH'),Card('QD'),Card('JH'),Card('KS')])
        straight = Straight(hand)
        assert straight.get_rating().get() == (5, 14, 13, 12, 11, 10, 'Straight')

    def test_get_rating_ace_low(self):
        hand = Hand([Card('2S'),Card('AH'),Card('3D'),Card('5H'),Card('4S')])
        straight = Straight(hand)
        assert straight.get_rating().get() == (5, 5, 4, 3, 2, 1, 'Straight')
