from game import StartGame

class Test_GameStartGame:

    def test_startGameConstructor_noArgs(self):
        sg = StartGame()

        assert sg.gameId == 0
        assert sg.playerId == None

    def test_startGameConstructor_args(self):
        sg = StartGame('1', '2')

        assert sg.gameId == '1'
        assert sg.playerId == '2'

    def test_joinGameCreate(self):
        sg = StartGame('1').Start('2')

        assert sg.gameId == '1'
        assert sg.playerId == '2'
