from cards import Card, Hand, StraightFlush, Straight

class Test_StraightFlush():
 
    def test_isMatch_1(self):
        hand = Hand([Card('2H'),Card('4H'),Card('6H'),Card('5H'),Card('3H')])
        straight_flush = StraightFlush()
        assert straight_flush.is_match(hand) == True

    def test_isMatch_2(self):
        hand = Hand([Card('9H'),Card('KH'),Card('QH'),Card('JH'),Card('TH')])
        straight_flush = StraightFlush()
        assert straight_flush.is_match(hand) == True

    def test_isMatch_notStraight(self):
        hand = Hand([Card('2H'),Card('6H'),Card('5H'),Card('4H'),Card('7H')])
        straight_flush = StraightFlush()
        assert straight_flush.is_match(hand) == False

    def test_isMatch_notFlush(self):
        hand = Hand([Card('3H'),Card('6D'),Card('5H'),Card('4H'),Card('7H')])
        straight_flush = StraightFlush()
        assert straight_flush.is_match(hand) == False

    def test_getRating(self):
        hand = Hand([Card('4S'),Card('5S'),Card('8S'),Card('7S'),Card('6S')])
        straight_flush = StraightFlush()
        assert straight_flush.get_rating(hand) == (9, 8, 7, 6, 5, 4)

    def test_getRating_royalFlush(self):
        hand = Hand([Card('AS'),Card('TS'),Card('QS'),Card('JS'),Card('KS')])
        straight_flush = StraightFlush()
        assert straight_flush.get_rating(hand) == (10, 14, 13, 12, 11, 10)

    def test_getRating_aceLow(self):
        hand = Hand([Card('2S'),Card('AS'),Card('3S'),Card('5S'),Card('4S')])
        straight_flush = StraightFlush()
        assert straight_flush.get_rating(hand) == (9, 5, 4, 3, 2, 1)

    def test_isRoyalFlush_true(self):
        hand = Hand([Card('AS'),Card('TS'),Card('QS'),Card('JS'),Card('KS')])
        straight_flush = StraightFlush()
        is_straight_flush = straight_flush.is_match(hand)
        is_straight_to_the_ace = Straight().is_straight_to_the_ace(hand)
        assert straight_flush.is_royal_flush(hand) == (is_straight_flush and is_straight_to_the_ace)
