import game
import bowlRedis
import cards

class Test_RedisStartGame:

    def startGameConstructor(self):
        sg = bowlRedis.StartGame()
        assert sg.game_id == None
        assert sg.player_id == None
        
    def joinStartInit(self):
        sg = game.StartGame('1')
        s = sg.start('2')
        r = bowlRedis.StartGame()
        r.init(s)

        assert s.game_id == r.game_id
        assert s.player_id == r.player_id
        
    def startGameExecHost(self):
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
        
        assert r.execute() == True

    def startGameExecNonHost(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)
        r.game_id = 'TEST'
        r.execute()
        
        sg = game.StartGame('TEST')
        s = sg.start('3')
        r = bowlRedis.StartGame()
        r.init(s)
        
        assert r.execute() == False

    def startGameGetHostSuccess(self):
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

        assert r.Get('game-TEST-info', 'status') == '1'

        statuses = r.Get('game-TEST-status')
        filtered = {k:v for k, v in statuses.iteritems() if v == '0'}.items()

        assert len(filtered) == 0

    def startGameGetNonHostFailure(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)
        r.game_id = 'TEST'
        r.execute()
        
        sg = game.StartGame('TEST')
        s = sg.start('3')
        r = bowlRedis.StartGame()
        r.init(s)
        r.game_id = 'TEST'
        r.execute()

        assert r.Get('game-TEST-info', 'status') == '0'

        statuses = r.Get('game-TEST-status')
        filtered = {k:v for k, v in statuses.iteritems() if v == '0'}.items()

        assert len(filtered) > 0
