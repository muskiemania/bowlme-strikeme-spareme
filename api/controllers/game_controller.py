import cherrypy
import json
import game
import viewmodels
import bowl_redis
import bowl_redis_dto
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
        gameVerified = game.Verify.verify_game_by_id(decoded['gameId'])
        playerVerified = game.Verify.verify_player_in_game(decoded['gameId'], decoded['playerId'])

        # hack to change player status
        #draw_cards = bowl_redis.DrawCards(decoded['gameId'], decoded['playerId'])
        #draw_cards.changePlayerStatus(bowl_redis_dto.PlayerStatus.FINISHED)
        
        my_game = game.Game.get(game_id=decoded['gameId'], player_id=decoded['playerId'])
        my_game.setGameKey(decoded['key'])
        
        return my_game.json()
