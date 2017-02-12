
from cards import Card, Hand, HighCard

class Test_HighCard():

    def test_isMatch_fiveCards(self):
        hand = Hand([Card('2H'),Card('4S'),Card('8C'),Card('QH'),Card('TD')])
        highCard = HighCard()
        assert highCard.IsMatch(hand) == True

    def test_isMatch_single(self):
        hand = Hand([Card('9H')])
        highCard = HighCard()
        assert highCard.IsMatch(hand) == True

    def test_isMatch_none(self):
        hand = Hand([])
        highCard = HighCard()
        assert highCard.IsMatch(hand) == True

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('4H'),Card('6D'),Card('8H'),Card('AS')])
        highCard = HighCard()
        assert highCard.GetRating(hand) == (1, 14, 8, 6, 4, 2)

    def test_getRating_partial(self):
        hand = Hand([Card('2S'),Card('KH'),Card('3D')])
        highCard = HighCard()
        assert highCard.GetRating(hand) == (1, 13, 3, 2, 0, 0)

    def test_getRating_none(self):
        hand = Hand([])
        highCard = HighCard()
        assert highCard.GetRating(hand) == (1, 0, 0, 0, 0, 0)
