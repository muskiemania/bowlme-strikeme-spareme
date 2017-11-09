import cherrypy
import json
import game
import viewmodels
import bowl_redis
import bowl_redis_dto
from . import Helpers

class ResultsController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET'
        return json.dumps({ 'ok': True })

    @cherrypy.expose
    def results(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)
        gameVerified = game.Verify.verify_game_by_id(decoded['gameId'])
        playerVerified = game.Verify.verify_player_in_game(decoded['gameId'], decoded['playerId'])

        results = game.Results.get(game_id=decoded['gameId'])
        results.setGameKey(decoded['key'])
        
        return results.json()
