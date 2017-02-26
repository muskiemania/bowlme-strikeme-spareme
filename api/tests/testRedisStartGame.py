import game
import bowlRedis
import cards

class Test_RedisStartGame:

    def test_startGameConstructor(self):
        sg = bowlRedis.StartGame()
        assert sg.gameId == None
        assert sg.playerId == None
        
    def test_joinStartInit(self):
        sg = game.StartGame('1')
        s = sg.Start('2')
        r = bowlRedis.StartGame()
        r.Init(s)

        assert s.gameId == r.gameId
        assert s.playerId == r.playerId
        
    def test_startGameExecHost(self):
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
        
        assert r.Exec() == True

    def test_startGameExecNonHost(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)
        r.gameId = 'TEST'
        r.Exec()
        
        sg = game.StartGame('TEST')
        s = sg.Start('3')
        r = bowlRedis.StartGame()
        r.Init(s)
        
        assert r.Exec() == False

    def test_startGameGetHostSuccess(self):
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

        assert r.Get('game-TEST-info', 'status') == '1'

        statuses = r.Get('game-TEST-status')
        filtered = {k:v for k,v in statuses.iteritems() if v == '0'}.items()

        assert len(filtered) == 0

    def test_startGameGetNonHostFailure(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)
        r.gameId = 'TEST'
        r.Exec()
        
        sg = game.StartGame('TEST')
        s = sg.Start('3')
        r = bowlRedis.StartGame()
        r.Init(s)
        r.gameId = 'TEST'
        r.Exec()

        assert r.Get('game-TEST-info', 'status') == '0'

        statuses = r.Get('game-TEST-status')
        filtered = {k:v for k,v in statuses.iteritems() if v == '0'}.items()

        assert len(filtered) > 0
