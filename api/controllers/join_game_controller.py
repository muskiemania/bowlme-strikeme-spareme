import cherrypy
import json
import game

class JoinGameController(object):

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
    def join(self):
        game_id = cherrypy.request.json['gameId']
        player_name = cherrypy.request.json['playerName']
        return game.JoinGame.join(game_id, player_name).json()
