import cherrypy
import json
import game
import viewmodels
from bowl_redis_dto import GameStatus, PlayerStatus
from . import Helpers
import traceback

class DiscardCardsController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({'ok': True})

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def discard(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''
        discard_cards = cherrypy.request.json['cards'] or []

        decoded = Helpers().decode_jwt(x_header)
        game_id = decoded['gameId']
        player_id = decoded['playerId']

        verify_game = game.Verify.verify_game_by_id
        verified_game_statuses = [GameStatus.STARTED]
        verify_player = game.Verify.verify_player_in_game
        verified_player_statuses = [PlayerStatus.DEALT, PlayerStatus.MUST_DISCARD]

        game_verified = verify_game(game_id, verified_game_statuses)
        player_verified = verify_player(game_id, player_id, verified_player_statuses)

        if game_verified and player_verified:
            try:
                game.DiscardCards.discard(game_id, player_id, discard_cards)
            except Exception as e:
                print traceback.print_exc()

        else:
            'verification failed'

        my_game = game.Game.get(game_id=game_id, player_id=player_id)
        my_game.setGameKey(decoded['key'])

        return my_game.json()
