from cards import Card, Flush, Hand

class Test_Flush():

    def test_isMatch_flush(self):
        hand = Hand([Card('2H'),Card('4H'),Card('5H'),Card('JH'),Card('AH')])
        flush = Flush()
        assert flush.IsMatch(hand) == True

    def test_isMatch_notEnoughCards(self):
        hand = Hand([Card('2H'),Card('4H'),Card('JH'),Card('AH')])
        flush = Flush()
        assert flush.IsMatch(hand) == False

    def test_isMatch_notAFlush(self):
        hand = Hand([Card('2S'),Card('4H'),Card('5H'),Card('JH'),Card('AH')])
        flush = Flush()
        assert flush.IsMatch(hand) == False

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('4H'),Card('5H'),Card('JH'),Card('KH')])
        flush = Flush()
        assert flush.GetRating(hand) == (6, 13, 11, 5, 4, 2)
