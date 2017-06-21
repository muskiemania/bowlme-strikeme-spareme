from game import CreateGame
import cards

class Test_GameCreateGame:

    def test_createGameConstructor_noArgs(self):
        g = CreateGame()

        assert g.game_id == 0
        assert g.host == None
        assert g.players == None
        assert g.deck == None
        assert g.discard == None
        assert g.status == 0

    def test_createGameCreateGameId(self):
        g = CreateGame()
        id = g.create_game_id('justin', 'key')
        assert id == '1dd8752235b0f14436f3940d4df5cae4'
        
    def test_createGameConstructor_args(self):
        d = cards.Deck()
        g = CreateGame(game_id = 1, host = 'Me', players = ['Me'], deck = d, discard = [], status = 1)

        assert g.game_id == 1
        assert g.host == 'Me'
        assert len(g.players) == 1 and g.players[0] == 'Me'
        assert len(g.deck.cards) == len(d.cards)
        assert len(g.discard) == 0
        assert g.status == 1

    def test_createGameCreate(self):
        g = CreateGame().create(host_name='justin',hash_key='key')

        assert g.game_id == CreateGame().create_game_id(host_name='justin', hash_key='key')
        assert len(g.players.keys()) == 1 and g.host in g.players.keys()
        assert g.players[g.host]['player_name'] == 'justin'
        assert len(g.deck.cards) == 52
        assert len(g.discard) == 0
        assert g.status == 0
