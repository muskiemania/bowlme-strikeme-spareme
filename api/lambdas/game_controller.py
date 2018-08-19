import cherrypy
import json
import game
from . import Helpers

class GameController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET'
        return json.dumps({ 'ok': True })

    @cherrypy.expose
    def game(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)

        game_id = decoded['gameId']
        player_id = decoded['playerId']

        #game_verified = game.Verify.verify_game_by_id(game_id)
        #player_verified = game.Verify.verify_player_in_game(game_id, player_id)

        # hack to change player status
        #draw_cards = bowl_redis.DrawCards(decoded['gameId'], decoded['playerId'])
        #draw_cards.changePlayerStatus(bowl_redis_dto.PlayerStatus.FINISHED)

        my_game = game.Game.get(game_id=game_id, player_id=player_id)
        my_game.setGameKey(decoded['key'])

        return my_game.json()
