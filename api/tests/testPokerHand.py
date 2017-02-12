from cards import Card,Hand,PokerHand
import pytest

class Test_PokerHand():
    def test_sortCards(self):
        hand = Hand(cards=[Card('2S'),Card('4H'),Card('3D')])
        PokerHand.sortCards(hand)
        assert hand.ShowCards() == ['4H','3D','2S']

        
    def test_cardTally(self):
        hand = Hand(cards=[Card('2S'),Card('3D'),Card('2D'),Card('2H')])
        cardDict = PokerHand.cardTally(hand)
        
        assert 2 in cardDict.keys()
        assert 3 in cardDict.keys()
        assert len(cardDict[2]) == 3
        assert len(cardDict[3]) == 1
