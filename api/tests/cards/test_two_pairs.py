import unittest
import cards.hand
import cards.card
import cards.two_pairs

class Test_TwoPairs(unittest.TestCase):

    def test_is_match_two_pairs(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('3C'),
            cards.card.Card('JH'),
            cards.card.Card('JD')
        ])
        two_pairs = cards.two_pairs.TwoPairs(hand)
        self.assertTrue(two_pairs.is_match())

    def test_is_match_not_four_of_a_kind(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('2C'),
            cards.card.Card('2D'),
            cards.card.Card('JD')
        ])
        two_pairs = cards.two_pairs.TwoPairs(hand)
        self.assertFalse(two_pairs.is_match())

    def test_get_rating_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3D'),
            cards.card.Card('JH'),
            cards.card.Card('JS')
        ])
        two_pairs = cards.two_pairs.TwoPairs(hand)
        self.assertEqual(two_pairs.get_rating(), (3, 11, 2, 3, 99, 99, 'Two Pairs'))

    def test_get_rating_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3D'),
            cards.card.Card('3H'),
            cards.card.Card('JS')
        ])
        two_pairs = cards.two_pairs.TwoPairs(hand)
        self.assertEqual(two_pairs.get_rating(), (3, 3, 2, 11, 99, 99, 'Two Pairs'))

    def test_get_rating_partial(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3H'),
            cards.card.Card('3S')
        ])
        two_pairs = cards.two_pairs.TwoPairs(hand)
        self.assertEqual(two_pairs.get_rating(), (3, 3, 2, 0, 99, 99, 'Two Pairs'))
