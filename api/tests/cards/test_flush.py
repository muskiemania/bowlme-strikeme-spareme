from cards import Card, Flush, Hand

class Test_Flush():

    def test_isMatch_flush(self):
        hand = Hand([Card('2H'),Card('4H'),Card('5H'),Card('JH'),Card('AH')])
        flush = Flush(hand)
        assert flush.is_match() == True

    def test_isMatch_notEnoughCards(self):
        hand = Hand([Card('2H'),Card('4H'),Card('JH'),Card('AH')])
        flush = Flush(hand)
        assert flush.is_match() == False

    def test_isMatch_notAFlush(self):
        hand = Hand([Card('2S'),Card('4H'),Card('5H'),Card('JH'),Card('AH')])
        flush = Flush(hand)
        assert flush.is_match() == False

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('4H'),Card('5H'),Card('JH'),Card('KH')])
        flush = Flush(hand)
        assert flush.get_rating() == (6, 13, 11, 5, 4, 2)
