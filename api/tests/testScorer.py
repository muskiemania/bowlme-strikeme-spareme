import pytest
from cards import Card, Hand
import scoring

class Test_Scorer:
    def test_clearWinner(self):
        justin = Hand([Card('AH'), Card('AS'), Card('KH'), Card('TD'), Card('TC')])
        sarah = Hand([Card('KD'), Card('KS'), Card('TH'), Card('JD'), Card('4C')])
        playerHands = []
        playerHands.append(('Justin', justin))
        playerHands.append(('Sarah', sarah))

        ranked = scoring.Scorer.ScoreHands(playerHands)

        assert ranked[0][0] == 'Justin'
        assert ranked[0][1] == justin
        assert ranked[0][2] == (3, 14, 10, 13, 99, 99)
        assert ranked[0][3] == 1

        assert ranked[1][0] == 'Sarah'
        assert ranked[1][1] == sarah
        assert ranked[1][2] == (2, 13, 11, 10, 4, 99)
        assert ranked[1][3] == 2
    
