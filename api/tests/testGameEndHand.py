from game import EndHand

class Test_GameEndHand:

    def test_endHandConstructor_noArgs(self):
        eh = EndHand()

        assert eh.gameId == 0
        assert eh.playerId == None

    def test_endHandConstructor_args(self):
        eh = EndHand('1', '2')

        assert eh.gameId == '1'
        assert eh.playerId == '2'

    def test_endHandEnd(self):
        eh = EndHand('1').End('2')

        assert eh.gameId == '1'
        assert eh.playerId == '2'
