
from cards import Card, Hand, HighCard

class Test_HighCard():

    def test_isMatch_fiveCards(self):
        hand = Hand([Card('2H'),Card('4S'),Card('8C'),Card('QH'),Card('TD')])
        high_card = HighCard()
        assert high_card.is_match(hand) == True

    def test_isMatch_single(self):
        hand = Hand([Card('9H')])
        high_card = HighCard()
        assert high_card.is_match(hand) == True

    def test_isMatch_none(self):
        hand = Hand([])
        high_card = HighCard()
        assert high_card.is_match(hand) == True

    def test_getRating(self):
        hand = Hand([Card('2S'),Card('4H'),Card('6D'),Card('8H'),Card('AS')])
        high_card = HighCard()
        assert high_card.get_rating(hand) == (1, 14, 8, 6, 4, 2)

    def test_getRating_partial(self):
        hand = Hand([Card('2S'),Card('KH'),Card('3D')])
        high_card = HighCard()
        assert high_card.get_rating(hand) == (1, 13, 3, 2, 0, 0)

    def test_getRating_none(self):
        hand = Hand([])
        high_card = HighCard()
        assert high_card.get_rating(hand) == (1, 0, 0, 0, 0, 0)
