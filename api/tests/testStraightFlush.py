from cards import Card, Hand, StraightFlush, Straight

class Test_StraightFlush():
 
    def test_is_match_1(self):
        hand = Hand([Card('2H'),Card('4H'),Card('6H'),Card('5H'),Card('3H')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.is_match() == True

    def test_is_match_2(self):
        hand = Hand([Card('9H'),Card('KH'),Card('QH'),Card('JH'),Card('TH')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.is_match() == True

    def test_is_match_not_straight(self):
        hand = Hand([Card('2H'),Card('6H'),Card('5H'),Card('4H'),Card('7H')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.is_match() == False

    def test_is_match_not_flush(self):
        hand = Hand([Card('3H'),Card('6D'),Card('5H'),Card('4H'),Card('7H')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.is_match() == False

    def test_get_rating(self):
        hand = Hand([Card('4S'),Card('5S'),Card('8S'),Card('7S'),Card('6S')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.get_rating() == (9, 8, 7, 6, 5, 4)

    def test_get_rating_royal_flush(self):
        hand = Hand([Card('AS'),Card('TS'),Card('QS'),Card('JS'),Card('KS')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.get_rating() == (10, 14, 13, 12, 11, 10)

    def test_get_rating_ace_low(self):
        hand = Hand([Card('2S'),Card('AS'),Card('3S'),Card('5S'),Card('4S')])
        straight_flush = StraightFlush(hand)
        assert straight_flush.get_rating() == (9, 5, 4, 3, 2, 1)

    def test_is_royal_flush_true(self):
        hand = Hand([Card('AS'),Card('TS'),Card('QS'),Card('JS'),Card('KS')])
        straight_flush = StraightFlush(hand)
        is_straight_flush = straight_flush.is_match()
        is_straight_to_the_ace = Straight(hand).is_straight_to_the_ace()
        assert straight_flush.is_royal_flush() == (is_straight_flush and is_straight_to_the_ace)
