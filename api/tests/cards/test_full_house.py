import unittest
import cards.card
import cards.hand
import cards.full_house

class Test_FullHouse(unittest.TestCase):

    def test_is_match_full_house_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('2C'),
            cards.card.Card('JH'),
            cards.card.Card('JD')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertTrue(full_house.is_match())

    def test_is_match_full_house_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2S'),
            cards.card.Card('JC'),
            cards.card.Card('JH'),
            cards.card.Card('JD')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertTrue(full_house.is_match())

    def test_is_match_not_four_of_a_kind(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2C'),
            cards.card.Card('2D'),
            cards.card.Card('2S'),
            cards.card.Card('3D')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertFalse(full_house.is_match())

    def test_is_match_not_three_of_a_kind(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2C'),
            cards.card.Card('2D'),
            cards.card.Card('4S'),
            cards.card.Card('3D')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertFalse(full_house.is_match())

    def test_is_match_not_two_pairs(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('2C'),
            cards.card.Card('4D'),
            cards.card.Card('4S'),
            cards.card.Card('3D')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertFalse(full_house.is_match())

    def test_get_rating_high(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('2D'),
            cards.card.Card('JH'),
            cards.card.Card('JS')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertEqual(full_house.get_rating(), (7, 2, 11, 99, 99, 99, 'Full House'))

    def test_get_rating_low(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('2H'),
            cards.card.Card('JD'),
            cards.card.Card('JH'),
            cards.card.Card('JS')
        ])
        full_house = cards.full_house.FullHouse(hand)
        self.assertEqual(full_house.get_rating(), (7, 11, 2, 99, 99, 99, 'Full House'))
