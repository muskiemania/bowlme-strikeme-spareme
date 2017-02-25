import game
import bowlRedis
import cards

class Test_RedisCreateGame:

    def test_createGameConstructor(self):
        r = bowlRedis.CreateGame()
        assert r.gameId == None
        assert r.host == None
        assert r.players == None
        assert r.deck == None
        assert r.discard == None
        assert r.status == None
        
    def test_createGameInit(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)

        assert g.gameId == r.gameId
        assert g.host == r.host
        assert g.players == r.players
        assert cards.Deck.ShowCards(g.deck.cards) == r.deck
        assert g.discard == r.discard
        assert g.status == r.status
        
    def test_createGameExec(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)
        
        assert r.Exec() == True

    def test_createGameGet(self):
        cg = game.CreateGame()
        g = cg.Create('justin','keys')
        r = bowlRedis.CreateGame()
        r.Init(g)
        r.gameId = 'TEST'
        r.Exec()

        assert r.Get('game-TEST-deck') == r.deck
        assert r.Get('game-TEST-info', 'host') == r.host
        assert r.Get('game-TEST-info', 'status') == str(r.status)
        assert r.Get('game-TEST-name', r.host) == 'justin'
        assert r.Get('game-TEST-status', r.host) == str(0)
