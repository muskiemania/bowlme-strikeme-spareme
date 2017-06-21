import game
import bowlRedis
import cards

class Test_RedisCreateGame:

    def test_createGameConstructor(self):
        r = bowlRedis.CreateGame()
        assert r.game_id == None
        assert r.host == None
        assert r.players == None
        assert r.deck == None
        assert r.discard == None
        assert r.status == None
        
    def test_createGameInit(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)

        assert g.game_id == r.game_id
        assert g.host == r.host
        assert g.players == r.players
        assert cards.Deck.show_cards(g.deck.cards) == r.deck
        assert g.discard == r.discard
        assert g.status == r.status
        
    def test_createGameExec(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)
        
        assert r.execute() == True

    def test_createGameGet(self):
        cg = game.CreateGame()
        g = cg.create('justin','keys')
        r = bowlRedis.CreateGame()
        r.init(g)
        r.game_id = 'TEST'
        r.execute()

        assert r.get('game-TEST-deck') == r.deck
        assert r.get('game-TEST-info', 'host') == r.host
        assert r.get('game-TEST-info', 'status') == str(r.status)
        assert r.get('game-TEST-name', r.host) == 'justin'
        assert r.get('game-TEST-status', r.host) == str(0)
