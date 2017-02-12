from cards import Card, Hand, StraightFlush, Straight

class Test_StraightFlush():
 
    def test_isMatch(self):
        hand = Hand([Card('2H'),Card('4H'),Card('6H'),Card('5H'),Card('3H')])
        straightFlush = StraightFlush()
        assert straightFlush.IsMatch(hand) == True

    def test_isMatch_notStraight(self):
        hand = Hand([Card('2H'),Card('6H'),Card('5H'),Card('4H'),Card('7H')])
        straightFlush = StraightFlush()
        assert straightFlush.IsMatch(hand) == False

    def test_isMatch_notFlush(self):
        hand = Hand([Card('3H'),Card('6D'),Card('5H'),Card('4H'),Card('7H')])
        straightFlush = StraightFlush()
        assert straightFlush.IsMatch(hand) == False

    def test_getRating(self):
        hand = Hand([Card('4S'),Card('5S'),Card('8S'),Card('7S'),Card('6S')])
        straightFlush = StraightFlush()
        assert straightFlush.GetRating(hand) == (9, 8, 7, 6, 5, 4)

    def test_getRating_royalFlush(self):
        #This is actually a royal flush
        hand = Hand([Card('AS'),Card('TS'),Card('QS'),Card('JS'),Card('KS')])
        straightFlush = StraightFlush()
        assert straightFlush.GetRating(hand) == (10, 14, 13, 12, 11, 10)

    def test_getRating_aceLow(self):
        hand = Hand([Card('2S'),Card('AS'),Card('3S'),Card('5S'),Card('4S')])
        straightFlush = StraightFlush()
        assert straightFlush.GetRating(hand) == (9, 5, 4, 3, 2, 1)

    def test_isRoyalFlush_true(self):
        hand = Hand([Card('AS'),Card('TS'),Card('QS'),Card('JS'),Card('KS')])
        straightFlush = StraightFlush()
        isStraightFlush = straightFlush.IsMatch(hand)
        isHighStraight = Straight().IsHighStraight(hand)
        assert straightFlush.IsRoyalFlush(hand) == (isStraightFlush and isHighStraight)
