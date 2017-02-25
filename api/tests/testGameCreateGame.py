from game import CreateGame
import cards

class Test_GameCreateGame:

    def test_createGameConstructor_noArgs(self):
        g = CreateGame()

        assert g.gameId == 0
        assert g.host == None
        assert g.players == None
        assert g.deck == None
        assert g.discard == None
        assert g.status == 0

    def test_createGameCreateGameId(self):
        g = CreateGame()
        id = g.CreateGameId('justin', 'key')
        assert id == '1dd8752235b0f14436f3940d4df5cae4'
        
    def test_createGameConstructor_args(self):
        d = cards.Deck()
        g = CreateGame(gameId = 1, host = 'Me', players = ['Me'], deck = d, discard = [], status = 1)

        assert g.gameId == 1
        assert g.host == 'Me'
        assert len(g.players) == 1 and g.players[0] == 'Me'
        assert len(g.deck.cards) == len(d.cards)
        assert len(g.discard) == 0
        assert g.status == 1

    def test_createGameCreate(self):
        g = CreateGame().Create(hostName='justin',hashKey='key')

        assert g.gameId == CreateGame().CreateGameId(hostName='justin',hashKey='key')
        assert len(g.players.keys()) == 1 and g.host in g.players.keys()
        assert g.players[g.host]['playerName'] == 'justin'
        assert len(g.deck.cards) == 52
        assert len(g.discard) == 0
        assert g.status == 0

        
        
