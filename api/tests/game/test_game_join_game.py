from game import CreatePlayer, JoinGame
import cards

class Test_GameJoinGame:

    def _test_joinGameConstructor_noArgs(self):
        g = JoinGame()

        assert g.game_id == 0
        assert g.player == None

    def _test_joinGameConstructor_args(self):
        p = CreatePlayer('player two', '1')
        j = JoinGame(game_id = '1', player = p)

        assert j.game_id == '1'
        assert j.player.player_name == 'player two'
        assert j.player.status == 0

    #def test_joinGame_join(self):
    #    gameDto = JoinGame.join('1', 'player two')

    #    print gameDto.__dict__
        
    #    assert gameDto.game_id == '1'
    #    assert 'player two' in map(lambda p: p.player_name, gameDto.players)
        #assert gameDto.player.status == 0

        
        
