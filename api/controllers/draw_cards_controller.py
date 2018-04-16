import cherrypy
import json
import game
import viewmodels
from bowl_redis_dto import GameStatus, PlayerStatus
from . import Helpers
import traceback

class DrawCardsController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        return json.dumps({ 'ok': True })
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def draw(self):

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''
        number_of_cards = cherrypy.request.json['numberOfCards'] or 1

        decoded = Helpers().decode_jwt(x_header)
        game_id = decoded['gameId']
        player_id = decoded['playerId']

        verify_game = game.Verify.verify_game_by_id
        verify_player = game.Verify.verify_player_in_game
        
        game_verified = verify_game(game_id, [GameStatus.STARTED])
        player_verified = verify_player(game_id, player_id, [PlayerStatus.DEALT])

        if game_verified and player_verified:
            try:
                game.DrawCards.draw(game_id, player_id, number_of_cards)
            except Exception as e:
                print 'whats the matter?'
                print e
                print traceback.format_exc()
        else:
            print 'game or player not verified'

        my_game = game.Game.get(game_id=game_id, player_id=player_id)
        my_game.setGameKey(decoded['key'])

        return my_game.json()
