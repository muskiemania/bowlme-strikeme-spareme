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
        return json.dumps({'ok': True})

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def finish(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''

        decoded = Helpers().decode_jwt(x_header)
        game_id = decoded['gameId']
        player_id = decoded['playerId']

        verify_game = game.Verify.verify_game_by_id
        verify_player = game.Verify.verify_player_in_game
        game_verified = verify_game(game_id, [GameStatus.STARTED])
        player_verified = verify_player(game_id, player_id, [PlayerStatus.DEALT])

        if game_verified and player_verified:
            try:
                game.Finish.execute(game_id, player_id)
            except Exception as e:
                print 'finish did not work'
                print str(e)

        my_game = game.Game.get(game_id=game_id, player_id=player_id)
        my_game.setGameKey(decoded['key'])

        return my_game.json()
