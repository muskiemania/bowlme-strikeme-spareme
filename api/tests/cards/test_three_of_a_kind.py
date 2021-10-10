import unittest
import cards.card
import cards.hand
import cards.three_of_a_kind

class Test_ThreeOfAKind(unittest.TestCase):

    def test_is_match_three_of_a_kind(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('3C'),
            cards.card.Card('JH'),
            cards.card.Card('2D')
        ])
        three_of_a_kind = cards.three_of_a_kind.ThreeOfAKind(hand)
        self.assertTrue(three_of_a_kind.is_match())

    def test_get_rating(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3D'),
            cards.card.Card('JH'),
            cards.card.Card('2C')
        ])
        three_of_a_kind = cards.three_of_a_kind.ThreeOfAKind(hand)
        self.assertEqual(three_of_a_kind.get_rating(), (4, 2, 11, 3, 99, 99, 'Three-Of-A-Kind'))

    def test_get_rating_full_house(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('3D'),
            cards.card.Card('3H'),
            cards.card.Card('3S')
        ])
        three_of_a_kind = cards.three_of_a_kind.ThreeOfAKind(hand)
        self.assertEqual(three_of_a_kind.get_rating(), (4, 3, 2, 99, 99, 99, 'Three-Of-A-Kind'))

    def test_get_rating_partial_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('JH'),
            cards.card.Card('2C')
        ])
        three_of_a_kind = cards.three_of_a_kind.ThreeOfAKind(hand)
        self.assertEqual(three_of_a_kind.get_rating(), (4, 2, 11, 0, 99, 99, 'Three-Of-A-Kind'))

    def test_get_rating_partial_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('2C')
        ])
        three_of_a_kind = cards.three_of_a_kind.ThreeOfAKind(hand)
        self.assertEqual(three_of_a_kind.get_rating(), (4, 2, 0, 0, 99, 99, 'Three-Of-A-Kind'))
