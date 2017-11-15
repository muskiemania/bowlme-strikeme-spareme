import cherrypy
import json
import game
import viewmodels
from bowl_redis_dto import GameStatus, PlayerStatus
from . import Helpers

class FinishGameController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({ 'ok': True })
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def finish(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)
        gameVerified = game.Verify.verify_game_by_id(decoded['gameId'], [GameStatus.STARTED])
        playerVerified = game.Verify.verify_player_in_game(decoded['gameId'], decoded['playerId'], [PlayerStatus.DEALT])

        if gameVerified and playerVerified:
            try:
                game.Finish.execute(decoded['gameId'], decoded['playerId'])
            except Exception as e:
                print 'finish did not work'
                print str(e)
                pass
                
        my_game = game.Game.get(game_id=decoded['gameId'], player_id=decoded['playerId'])
        my_game.setGameKey(decoded['key'])
        
        return my_game.json()
