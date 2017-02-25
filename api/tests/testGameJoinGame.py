from game import CreatePlayer, JoinGame
import cards

class Test_GameJoinGame:

    def test_joinGameConstructor_noArgs(self):
        g = JoinGame()

        assert g.gameId == 0
        assert g.player == None

    def test_joinGameConstructor_args(self):
        p = CreatePlayer('player two', '1')
        j = JoinGame(gameId = '1', player = p)

        assert j.gameId == '1'
        assert j.player.playerName == 'player two'
        assert j.player.status == 0

    def test_joinGameCreate(self):
        j = JoinGame('1').Join('player two')

        assert j.gameId == '1'
        assert j.player.playerName == 'player two'
        assert j.player.status == 0

        
        
