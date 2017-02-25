import game
import bowlRedis
import cards

class Test_RedisJoinGame:

    def test_joinGameConstructor(self):
        r = bowlRedis.JoinGame()
        assert r.gameId == None
        assert r.player == None
        
    def test_joinGameInit(self):
        jg = game.JoinGame('1')
        j = jg.Join('player two')
        r = bowlRedis.JoinGame()
        r.Init(j)

        assert j.gameId == r.gameId
        assert j.player == r.player
        
    def test_createGameExec(self):
        jg = game.JoinGame('1')
        j = jg.Join('player two')
        r = bowlRedis.JoinGame()
        r.Init(j)
        
        assert r.Exec() == True

    def test_joinGameGet(self):
        jg = game.JoinGame('1')
        j = jg.Join('player two')
        r = bowlRedis.JoinGame()
        r.Init(j)
        r.gameId = 'TEST'
        r.Exec()

        assert r.Get('game-TEST-name', r.player.playerId) == 'player two'
        assert r.Get('game-TEST-status', r.player.playerId) == str(0)
