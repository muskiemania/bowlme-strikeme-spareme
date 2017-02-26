import game
import bowlRedis
import cards

class Test_RedisEndHand:

    def test_endHandConstructor(self):
        eh = bowlRedis.EndHand()
        assert eh.gameId == None
        assert eh.playerId == None
        
    def test_endHandInit(self):
        eh = game.EndHand('1')
        e = eh.End('2')
        r = bowlRedis.EndHand()
        r.Init(e)

        assert e.gameId == r.gameId
        assert e.playerId == r.playerId
        
    def test_endHandExec(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)
        r.gameId = 'TEST'
        r.Exec()
        
        sg = game.StartGame('TEST')
        s = sg.Start('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.StartGame()
        r.Init(s)

        eh = game.EndHand('TEST')
        e = eh.End('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.EndHand()
        r.Init(e)
        
        assert r.Exec() == True

    def test_endHandGet(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)
        r.gameId = 'TEST'
        r.Exec()
        
        sg = game.StartGame('TEST')
        s = sg.Start('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.StartGame()
        r.Init(s)
        r.gameId = 'TEST'
        r.Exec()
        
        eh = game.EndHand('TEST')
        h = eh.End('d6f14920aa9e0e3098cb9903ab5a1cf8')
        r = bowlRedis.EndHand()
        r.Init(h)
        r.gameId = 'TEST'

        assert r.Get('game-TEST-status', 'd6f14920aa9e0e3098cb9903ab5a1cf8') == '1'

        r.Exec()

        assert r.Get('game-TEST-status', 'd6f14920aa9e0e3098cb9903ab5a1cf8') == '0'
