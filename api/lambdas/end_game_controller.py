import cherrypy
import json
import game
from bowl_redis_dto import GameStatus
from . import Helpers
import traceback

class EndGameController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({'ok': True})

    @cherrypy.expose
    def end(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)
        game_id = decoded['gameId']
        player_id = decoded['playerId']

        game_verified = game.Verify.verify_game_by_id(game_id, [GameStatus.STARTED])
        player_verified = game.Verify.verify_player_in_game(game_id, player_id)
        player_is_host = game.Verify.verify_player_is_host(game_id, player_id)

        if game_verified and player_verified and player_is_host:
            try:
                game.EndGame.end(game_id)
                print 'game ended'
            except Exception as e:
                print 'something went wrong'
                print e
                print e.args
                print traceback.format_exc()
        else:
            print 'verification failed'

        results = game.Results.get(game_id=decoded['gameId'], player_id=decoded['playerId'])
        results.setGameKey(decoded['key'])

        return results.json()
