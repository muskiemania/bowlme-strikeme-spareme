from cards import Card,Hand,PokerHand
import pytest

class Test_PokerHand():
    def test_sortCards(self):
        hand = Hand(cards=[Card('2S'),Card('4H'),Card('3D')])
        PokerHand.sort_cards(hand)
        assert hand.show_cards() == ['4H','3D','2S']

        
    def test_cardTally(self):
        hand = Hand(cards=[Card('2S'),Card('3D'),Card('2D'),Card('2H')])
        card_dictionary = PokerHand.card_tally(hand)
        
        assert 2 in card_dictionary.keys()
        assert 3 in card_dictionary.keys()
        assert len(card_dictionary[2]) == 3
        assert len(card_dictionary[3]) == 1
