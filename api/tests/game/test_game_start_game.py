from game import StartGame

class Test_GameStartGame:

    def test_startGameConstructor_noArgs(self):
        sg = StartGame()

        assert sg.game_id == 0
        assert sg.player_id == None

    def test_startGameConstructor_args(self):
        sg = StartGame('1', '2')

        assert sg.game_id == '1'
        assert sg.player_id == '2'

    def test_joinGameCreate(self):
        sg = StartGame('1').start('2')

        assert sg.game_id == '1'
        assert sg.player_id == '2'
