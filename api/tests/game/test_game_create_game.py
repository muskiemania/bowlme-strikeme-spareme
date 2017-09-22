from game import CreateGame
from bowl_redis_dto import GameStatus
import cards

class Test_GameCreateGame:

    def _test_createGameConstructor_noArgs(self):
        dto = CreateGame()

        assert dto == None

    def _test_createGameCreateGameId(self):
        g = CreateGame()
        id = g.create_game_id('justin', 'key')
        assert id == '1dd8752235b0f14436f3940d4df5cae4'
        
    def _test_createGameConstructor_args(self):
        d = cards.Deck()
        g = CreateGame(game_id = 1, host = 'Me', players = ['Me'], deck = d, discard = [], status = 1)

        assert g.game_id == 1
        assert g.host == 'Me'
        assert len(g.players) == 1 and g.players[0] == 'Me'
        assert len(g.deck.cards) == len(d.cards)
        assert len(g.discard) == 0
        assert g.status == 1

    def test_createGameCreate(self):
        gameDto = CreateGame.create(host_player_name='justin')
        #print dto.__dict__
        #assert g.game_id == CreateGame.create(host_player_name='justin')
        assert len(gameDto.players) == 1
        assert gameDto.host_player_name in map(lambda p: p.player_name, gameDto.players)
        assert gameDto.host_player_id in map(lambda p: p.player_id, gameDto.players)
        #assert dto.players[g.host]['player_name'] == 'justin'
        #assert g.deck.cards == None
        #assert g.discard == None
        assert gameDto.game_status == GameStatus.CREATED
