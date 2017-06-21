from game import CreatePlayer, JoinGame
import cards

class Test_GameJoinGame:

    def test_joinGameConstructor_noArgs(self):
        g = JoinGame()

        assert g.game_id == 0
        assert g.player == None

    def test_joinGameConstructor_args(self):
        p = CreatePlayer('player two', '1')
        j = JoinGame(game_id = '1', player = p)

        assert j.game_id == '1'
        assert j.player.player_name == 'player two'
        assert j.player.status == 0

    def test_joinGameCreate(self):
        j = JoinGame('1').join('player two')

        assert j.game_id == '1'
        assert j.player.player_name == 'player two'
        assert j.player.status == 0

        
        
