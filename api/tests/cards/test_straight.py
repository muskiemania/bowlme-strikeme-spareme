import unittest
import cards.card
import cards.hand
import cards.straight

class Test_Straight(unittest.TestCase):
 
    def test_is_match_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('2H'),
            cards.card.Card('3S'),
            cards.card.Card('6C'),
            cards.card.Card('5H'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_match())

    def test_is_match_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('9H'),
            cards.card.Card('KH'),
            cards.card.Card('QH'),
            cards.card.Card('JH'),
            cards.card.Card('TH')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_match())

    def test_is_match_not_enough_cards(self):
        hand = cards.hand.Hand([
            cards.card.Card('3H'),
            cards.card.Card('6C'),
            cards.card.Card('5H'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertFalse(straight.is_match())

    def test_is_match_ace_high(self):
        hand = cards.hand.Hand([
            cards.card.Card('TH'),
            cards.card.Card('JS'),
            cards.card.Card('KC'),
            cards.card.Card('AD'),
            cards.card.Card('QD')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_match())

    def test_is_match_ace_low(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('AS'),
            cards.card.Card('3C'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_match())

    def test_is_coherent_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('AS'),
            cards.card.Card('3C'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_coherent())
        
    def test_is_coherent_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('KH'),
            cards.card.Card('AS'),
            cards.card.Card('JC'),
            cards.card.Card('TD'),
            cards.card.Card('QD')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_coherent())
        
    def test_is_coherent_3(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('6S'),
            cards.card.Card('3C'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_coherent())
        
    def test_is_coherent_4(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('6S'),
            cards.card.Card('6C'),
            cards.card.Card('3D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_coherent())
        
    def test_is_coherent_5(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('AS'),
            cards.card.Card('KC'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertFalse(straight.is_coherent())

    def test_is_coherent_6(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('3C'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_coherent())

    def test_is_coherent_7(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('AS'),
            cards.card.Card('KC'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertFalse(straight.is_coherent())
    
    def test_is_low_straight_1(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('AS'),
            cards.card.Card('3C'),
            cards.card.Card('2D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertTrue(straight.is_low_straight())

    def test_is_low_straight_2(self):
        hand = cards.hand.Hand([
            cards.card.Card('5H'),
            cards.card.Card('2S'),
            cards.card.Card('6C'),
            cards.card.Card('3D'),
            cards.card.Card('4D')
        ])
        straight = cards.straight.Straight(hand)
        self.assertFalse(straight.is_low_straight())

    def test_is_low_straight_3(self):
        hand = cards.hand.Hand([
            cards.card.Card('AH'),
            cards.card.Card('TS'),
            cards.card.Card('JC'),
            cards.card.Card('KD'),
            cards.card.Card('QD')
        ])
        straight = cards.straight.Straight(hand)
        self.assertFalse(straight.is_low_straight())

    def test_get_rating(self):
        hand = cards.hand.Hand([
            cards.card.Card('4S'),
            cards.card.Card('5H'),
            cards.card.Card('8D'),
            cards.card.Card('7H'),
            cards.card.Card('6S')
        ])
        straight = cards.straight.Straight(hand)
        self.assertEqual(straight.get_rating(), (5, 8, 7, 6, 5, 4, 'Straight'))

    def test_get_rating_ace_high(self):
        hand = cards.hand.Hand([
            cards.card.Card('AS'),
            cards.card.Card('TH'),
            cards.card.Card('QD'),
            cards.card.Card('JH'),
            cards.card.Card('KS')
        ])
        straight = cards.straight.Straight(hand)
        self.assertEqual(straight.get_rating(), (5, 14, 13, 12, 11, 10, 'Straight'))

    def test_get_rating_ace_low(self):
        hand = cards.hand.Hand([
            cards.card.Card('2S'),
            cards.card.Card('AH'),
            cards.card.Card('3D'),
            cards.card.Card('5H'),
            cards.card.Card('4S')
        ])
        straight = cards.straight.Straight(hand)
        self.assertEqual(straight.get_rating(), (5, 5, 4, 3, 2, 1, 'Straight'))
