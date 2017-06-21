import game
import bowlRedis
import cards

class Test_RedisJoinGame:

    def test_joinGameConstructor(self):
        r = bowlRedis.JoinGame()
        assert r.game_id == None
        assert r.player == None
        
    def test_joinGameInit(self):
        jg = game.JoinGame('1')
        j = jg.join('player two')
        r = bowlRedis.JoinGame()
        r.init(j)

        assert j.game_id == r.game_id
        assert j.player == r.player
        
    def test_createGameExec(self):
        jg = game.JoinGame('1')
        j = jg.join('player two')
        r = bowlRedis.JoinGame()
        r.init(j)
        
        assert r.execute() == True

    def test_joinGameGet(self):
        jg = game.JoinGame('1')
        j = jg.join('player two')
        r = bowlRedis.JoinGame()
        r.init(j)
        r.game_id = 'TEST'
        r.execute()

        assert r.get('game-TEST-name', r.player.player_id) == 'player two'
        assert r.get('game-TEST-status', r.player.player_id) == str(0)
