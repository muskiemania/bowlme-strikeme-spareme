from game import EndHand

class Test_GameEndHand:

    def test_endHandConstructor_noArgs(self):
        eh = EndHand()

        assert eh.game_id == 0
        assert eh.player_id == None

    def test_endHandConstructor_args(self):
        eh = EndHand('1', '2')

        assert eh.game_id == '1'
        assert eh.player_id == '2'

    def test_endHandEnd(self):
        eh = EndHand('1').end('2')

        assert eh.game_id == '1'
        assert eh.player_id == '2'
