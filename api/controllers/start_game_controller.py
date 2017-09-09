import cherrypy
import json
import game

class StartGameController(object):

    def __init__(self):
        pass

    @cherrypy.config(**{'tools.response_headers.on': True, 'tools.response_headers.headers': [('Content-Language', 'en-US'), ('Content-Type', 'application/json')]})

    @cherrypy.expose
    def index(self):
        response = {}
        response['message'] = 'this controller is post only'
        return json.dumps(response)

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        game_id = cherrypy.request.json['gameId']
        host_player_id = cherrypy.request.json['hostPlayerId']
        return game.StartGame.start(game_id, host_player_id).json()
