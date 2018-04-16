import cherrypy
import json
import game
import viewmodels
from bowl_redis_dto import GameStatus
from . import Helpers
import traceback

class StartGameController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({'ok': True})

    @cherrypy.expose
    def start(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)
        game_id = decoded['gameId']
        player_id = decoded['playerId']

        game_verified = game.Verify.verify_game_by_id(game_id, [GameStatus.CREATED])
        player_verified = game.Verify.verify_player_in_game(game_id, player_id)
        player_is_host = game.Verify.verify_player_is_host(game_id, player_id)

        print 'X'
        print game_verified
        print player_verified
        print player_is_host
        print 'XX'

        if game_verified and player_verified and player_is_host:
            try:
                game.StartGame.start(game_id)
                print 'started ok'
            except Exception as e:
                print 'something went wrong'
                print e
                print e.args
                print traceback.format_exc()
        else:
            print 'verification failed'

        print 'hello there'
        my_game = game.Game.get(game_id=decoded['gameId'], player_id=decoded['playerId'])
        my_game.setGameKey(decoded['key'])
        
        return my_game.json()
