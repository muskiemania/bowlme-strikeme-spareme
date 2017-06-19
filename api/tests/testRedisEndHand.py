import game
import bowlRedis
import cards

class Test_RedisEndHand:

    def test_endHandConstructor(self):
        eh = bowlRedis.EndHand()
        assert eh.game_id == None
        assert eh.player_id == None
        
    def test_endHandInit(self):
        eh = game.EndHand('1')
        e = eh.end('2')
        r = bowlRedis.EndHand()
        r.init(e)

        assert e.game_id == r.game_id
        assert e.player_id == r.player_id
        
    def test_endHandExec(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)
        r.game_id = 'TEST'
        r.execute()
        
        sg = game.StartGame('TEST')
        s = sg.start('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.StartGame()
        r.init(s)

        eh = game.EndHand('TEST')
        e = eh.end('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.EndHand()
        r.init(e)
        
        assert r.execute() == True

    def test_endHandGet(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)
        r.game_id = 'TEST'
        r.execute()
        
        sg = game.StartGame('TEST')
        s = sg.start('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.StartGame()
        r.init(s)
        r.game_id = 'TEST'
        r.execute()
        
        eh = game.EndHand('TEST')
        h = eh.end('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.EndHand()
        r.init(h)
        r.game_id = 'TEST'

        assert r.get('game-TEST-status', 'd6f14920aa9e0e3098cb9903ab5a1cf8') == '1'

        r.execute()

        assert r.get('game-TEST-status', 'd6f14920aa9e0e3098cb9903ab5a1cf8') == '0'
