import cherrypy
import json
import game
import viewmodels
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

        #try:
        cookie_value = cherrypy.request.cookie[Helpers().get_cookie_name()].value
        decoded = Helpers().decode_jwt(cookie_value)

        my_game = game.Game.get(game_id=decoded['gameId'], player_id=decoded['playerId'])

        print my_game
        
        return my_game.json()
