import unittest
import cards.card
import cards.hand
import cards.poker_hand

class Test_PokerHand(unittest.TestCase):
    def test_sort_cards(self):
        hand = cards.hand.Hand(cards=[cards.card.Card('2S'),cards.card.Card('4H'),cards.card.Card('3D')])
        poker_hand = cards.poker_hand.PokerHand(hand)
        poker_hand.sort_cards()
        self.assertEqual(poker_hand.show_cards(), ['4H','3D','2S'])

        
    def test_card_tally(self):
        hand = cards.hand.Hand(cards=[cards.card.Card('2S'),cards.card.Card('3D'),cards.card.Card('2D'),cards.card.Card('2H')])
        poker_hand = cards.poker_hand.PokerHand(hand)
        card_dictionary = poker_hand.card_tally()
        
        self.assertIn(2, card_dictionary.keys())
        self.assertIn(3, card_dictionary.keys())
        self.assertEqual(len(card_dictionary[2]), 3)
        self.assertEqual(len(card_dictionary[3]), 1)
