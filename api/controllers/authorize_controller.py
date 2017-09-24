import cherrypy
import json
import game

class AuthorizeController(object):

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
    def verify(self):
        game_id = cherrypy.request.cookie['game_auth']
        player_id = cherrypy.request.cookie['player_auth']
        auth_response = game.Verify.verify(game_id, player_id)

        verify_response = {}
        if auth_response is not None:
            verify_response['gameId'] = auth_response.game_key;
            verify_response['playerId'] = auth_response.player_key;

        return verify_response.json()
    
