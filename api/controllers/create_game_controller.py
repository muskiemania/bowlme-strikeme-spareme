import cherrypy
import json
import game
from . import Helpers

class CreateGameController(object):

    def __init__(self):
        pass

    #@cherrypy.config(**{'tools.response_headers.on': True, 'tools.response_headers.headers': [('Content-Language', 'en-US'), ('Content-Type', 'application/json')]})

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'POST'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Accept, Content-Type'
        cherrypy.response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5000'
        cherrypy.response.headers['Access-Control-Allow-Credentials'] = 'true'
        return json.dumps({ 'ok': True })
        #response = {}
        #response['message'] = 'this controller is post only'
        #return json.dumps(response)

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def create(self):

        print '---'
        x = cherrypy.request.body.fp.read()
        print x
        print '---'
        
        host_player_name = cherrypy.request.json['playerName']

        #create game
        created_game = game.CreateGame.create(host_player_name)

        #create cookie
        if not created_game.is_game_id_zero():
            jwt = Helpers().get_jwt(created_game.get_jwt_data())
            cherrypy.response.cookie[Helpers().get_cookie_name()] = jwt
            cherrypy.response.cookie[Helpers().get_cookie_name()]['expires'] = 7200

        return created_game.json()
