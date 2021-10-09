import unittest
import cards.hand
import cards.flush
import cards.card

class Test_Flush(unittest.TestCase):

    def test_is_match_flush(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('4H'),
            cards.card.Card('5H'),
            cards.card.Card('JH'),
            cards.card.Card('AH')
        ])
        flush = cards.flush.Flush(hand)
        self.assertTrue(flush.is_match())

    def test_is_match_not_enough_cards(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('4H'),
            cards.card.Card('JH'),
            cards.card.Card('AH')
        ])
        flush = cards.flush.Flush(hand)
        self.assertFalse(flush.is_match())

    def test_is_match_not_a_flush(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('4H'),
            cards.card.Card('5H'),
            cards.card.Card('JH'),
            cards.card.Card('AH')
        ])
        flush = cards.flush.Flush(hand)
        self.assertFalse(flush.is_match())

    def test_get_rating(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('4H'),
            cards.card.Card('5H'),
            cards.card.Card('JH'),
            cards.card.Card('KH')
        ])
        flush = cards.flush.Flush(hand)
        self.assertEqual(flush.get_rating(), (6, 13, 11, 5, 4, 2, 'Flush'))
