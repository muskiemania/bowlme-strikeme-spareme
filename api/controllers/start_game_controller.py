import cherrypy
import json
import game
import viewmodels
from bowl_redis_dto import GameStatus
from . import Helpers

class StartGameController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({ 'ok': True })
    
    @cherrypy.expose
    def start(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)
        gameVerified = game.Verify.verify_game_by_id(decoded['gameId'], [GameStatus.CREATED])
        playerVerified = game.Verify.verify_player_in_game(decoded['gameId'], decoded['playerId'])
        playerIsHost = game.Verify.verify_player_is_host(decoded['gameId'], decoded['playerId'])

        print 'X'
        print gameVerified
        print playerVerified
        print playerIsHost
        print 'XX'
        
        if gameVerified and playerVerified and playerIsHost:
            try:
                game.StartGame.start(decoded['gameId'], decoded['playerId'])
                print 'started ok'
            except Exception as e:
                print 'something went wrong'
                print e
                print e.args
        else:
            'verification failed'

        print 'hello there'
        my_game = game.Game.get(game_id=decoded['gameId'], player_id=decoded['playerId'])
        my_game.setGameKey(decoded['key'])
        
        return my_game.json()
