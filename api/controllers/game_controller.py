import cherrypy
import json
import game

class GameController(object):

    def __init__(self):
        pass

    @cherrypy.config(**{'tools.response_headers.on': True, 'tools.response_headers.headers': [('Content-Language', 'en-US'), ('Content-Type', 'application/json')]})

    @cherrypy.expose
    def index(self, game_id, player_id):
        return game.Game.get(game_id, player_id).json()
