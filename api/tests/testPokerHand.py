from cards import Card,Hand,PokerHand
import pytest

class Test_PokerHand():
    def test_sortCards(self):
        hand = Hand(cards=[Card('2S'),Card('4H'),Card('3D')])
        pokerhand = PokerHand(hand)
        pokerhand.sort_cards()
        assert pokerhand.hand.show_cards() == ['4H','3D','2S']

        
    def test_cardTally(self):
        hand = Hand(cards=[Card('2S'),Card('3D'),Card('2D'),Card('2H')])
        pokerHand = PokerHand(hand)
        card_dictionary = pokerHand.card_tally()
        
        assert 2 in card_dictionary.keys()
        assert 3 in card_dictionary.keys()
        assert len(card_dictionary[2]) == 3
        assert len(card_dictionary[3]) == 1
