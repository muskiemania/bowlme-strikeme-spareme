
from cards import Card, Hand, HighCard

class Test_HighCard():

    def test_is_match_five_cards(self):
        hand = Hand([Card('2H'),Card('4S'),Card('8C'),Card('QH'),Card('TD')])
        high_card = HighCard(hand)
        assert high_card.is_match() == True

    def test_is_match_single(self):
        hand = Hand([Card('9H')])
        high_card = HighCard(hand)
        assert high_card.is_match() == True

    def test_is_atch_none(self):
        hand = Hand([])
        high_card = HighCard(hand)
        assert high_card.is_match() == True

    def test_get_rating(self):
        hand = Hand([Card('2S'),Card('4H'),Card('6D'),Card('8H'),Card('AS')])
        high_card = HighCard(hand)
        assert high_card.get_rating().get() == (1, 14, 8, 6, 4, 2, 'High Card')

    def test_get_rating_partial(self):
        hand = Hand([Card('2S'),Card('KH'),Card('3D')])
        high_card = HighCard(hand)
        assert high_card.get_rating().get() == (1, 13, 3, 2, 0, 0, 'High Card')

    def test_get_rating_none(self):
        hand = Hand([])
        high_card = HighCard(hand)
        assert high_card.get_rating().get() == (1, 0, 0, 0, 0, 0, 'High Card')
