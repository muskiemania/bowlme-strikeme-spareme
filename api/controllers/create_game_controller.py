import cherrypy
import json
import game

class CreateGameController(object):

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
    def create(self):
        host_player_name = cherrypy.request.json['host_player_name']
        return game.CreateGame.create(host_player_name).json()
