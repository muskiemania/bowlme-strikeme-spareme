import unittest
import cards.card
import cards.hand
import cards.high_card

class Test_HighCard(unittest.TestCase):

    def test_is_match_five_cards(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('4S'),
            cards.card.Card('8C'),
            cards.card.Card('QH'),
            cards.card.Card('TD')
        ])
        high_card = cards.high_card.HighCard(hand)
        self.assertTrue(high_card.is_match())

    def test_is_match_single(self):
        hand = cards.hand.Hand([cards.card.Card('9H')])
        high_card = cards.high_card.HighCard(hand)
        self.assertTrue(high_card.is_match())

    def test_is_match_none(self):
        hand = cards.hand.Hand([])
        high_card = cards.high_card.HighCard(hand)
        self.assertTrue(high_card.is_match())

    def test_get_rating(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('4H'),
            cards.card.Card('6D'),
            cards.card.Card('8H'),
            cards.card.Card('AS')
        ])
        high_card = cards.high_card.HighCard(hand)
        self.assertEqual(high_card.get_rating(), (1, 14, 8, 6, 4, 2, 'High Card'))

    def test_get_rating_partial(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('KH'),
            cards.card.Card('3D')
        ])
        high_card = cards.high_card.HighCard(hand)
        self.assertEqual(high_card.get_rating(), (1, 13, 3, 2, 0, 0, 'High Card'))

    def test_get_rating_none(self):
        hand = cards.hand.Hand([])
        high_card = cards.high_card.HighCard(hand)
        self.assertEqual(high_card.get_rating(), (1, 0, 0, 0, 0, 0, 'High Card'))
