import unittest
import cards.card
import cards.hand
import cards.one_pair

class Test_OnePair(unittest.TestCase):

    def test_is_match(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('3C'),
            cards.card.Card('4H'),
            cards.card.Card('JD')
        ])
        one_pair = cards.one_pair.OnePair(hand)
        self.assertTrue(one_pair.is_match())

    def test_is_match_partial(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('3C')
        ])
        one_pair = cards.one_pair.OnePair(hand)
        self.assertTrue(one_pair.is_match())

    def test_is_match_only(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S')
        ])
        one_pair = cards.one_pair.OnePair(hand)
        self.assertTrue(one_pair.is_match())

    def test_get_rating(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3D'),
            cards.card.Card('4H'),
            cards.card.Card('JS')
        ])
        one_pair = cards.one_pair.OnePair(hand)
        self.assertEqual(one_pair.get_rating(), (2, 2, 11, 4, 3, 99, 'One Pair'))

    def test_get_rating_partial(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3D')
        ])
        one_pair = cards.one_pair.OnePair(hand)
        self.assertEqual(one_pair.get_rating(), (2, 2, 3, 0, 0, 99, 'One Pair'))

    def test_get_rating_only(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H')
        ])
        one_pair = cards.one_pair.OnePair(hand)
        self.assertEqual(one_pair.get_rating(), (2, 2, 0, 0, 0, 99, 'One Pair'))
