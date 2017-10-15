import cherrypy
import json
import game
import viewmodels
from bowl_redis_dto import GameStatus, PlayerStatus
from . import Helpers

class DiscardCardsController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({ 'ok': True })
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def discard(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''
        discard_cards = cherrypy.request.json['cards'] or []

        decoded = Helpers().decode_jwt(x_header)
        gameVerified = game.Verify.verify_game_by_id(decoded['gameId'], [GameStatus.STARTED])
        playerVerified = game.Verify.verify_player_in_game(decoded['gameId'], decoded['playerId'], [PlayerStatus.DEALT])

        if gameVerified and playerVerified:
            try:
                game.DiscardCards.discard(decoded['gameId'], decoded['playerId'], discard_cards)
                print 'cards drawn ok'
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
