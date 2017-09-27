import cherrypy
import json
import game

class GameController(object):

    def __init__(self):
        pass

    @cherrypy.config(**{'tools.response_headers.on': True, 'tools.response_headers.headers': [('Content-Language', 'en-US'), ('Content-Type', 'application/json')]})

    @cherrypy.expose
    def index(self):

        #try:
        cookie_value = cherrypy.request.cookie[Helpers().get_cookie_name()].value
        decoded = Helpers().decode_jwt(cookie_value)

        my_game = game.Game(game_id=decoded['gameId'], player_id=decoded['playerId'])

        return my_game.json()
