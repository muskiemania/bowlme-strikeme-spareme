import unittest
import cards.card
import cards.hand
import cards.straight_flush

class Test_StraightFlush(unittest.TestCase):
 
    def test_is_match_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('4H'),
            cards.card.Card('6H'),
            cards.card.Card('5H'),
            cards.card.Card('3H')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertTrue(straight_flush.is_match())

    def test_is_match_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('9H'),
            cards.card.Card('KH'),
            cards.card.Card('QH'),
            cards.card.Card('JH'),
            cards.card.Card('TH')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertTrue(straight_flush.is_match())

    def test_is_match_not_straight(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('6H'),
            cards.card.Card('5H'),
            cards.card.Card('4H'),
            cards.card.Card('7H')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertFalse(straight_flush.is_match())

    def test_is_match_not_flush(self):
        hand = cards.hand.Hand([
            cards.card.Card('3H'),
            cards.card.Card('6D'),
            cards.card.Card('5H'),
            cards.card.Card('4H'),
            cards.card.Card('7H')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertFalse(straight_flush.is_match())

    def test_get_rating(self):
        hand = cards.hand.Hand([
            cards.card.Card('4S'),
            cards.card.Card('5S'),
            cards.card.Card('8S'),
            cards.card.Card('7S'),
            cards.card.Card('6S')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertEqual(straight_flush.get_rating(), (9, 8, 7, 6, 5, 4, 'Straight Flush'))

    def test_get_rating_royal_flush(self):
        hand = cards.hand.Hand([
            cards.card.Card('AS'),
            cards.card.Card('TS'),
            cards.card.Card('QS'),
            cards.card.Card('JS'),
            cards.card.Card('KS')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertEqual(straight_flush.get_rating(), (10, 14, 13, 12, 11, 10, 'Royal Flush'))

    def test_get_rating_ace_low(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('AS'),
            cards.card.Card('3S'),
            cards.card.Card('5S'),
            cards.card.Card('4S')
        ])
        straight_flush = cards.straight_flush.StraightFlush(hand)
        self.assertEqual(straight_flush.get_rating(), (9, 5, 4, 3, 2, 1, 'Straight Flush'))

