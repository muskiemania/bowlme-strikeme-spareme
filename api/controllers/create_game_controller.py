import cherrypy
import json
import game
import viewmodels
from . import Helpers

class CreateGameController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
        return json.dumps({ 'ok': True })

    @cherrypy.expose
    def verify(self):

        null_game = viewmodels.JoinGameModel(0, 0, None)
             
        if Helpers().get_cookie_name() not in cherrypy.request.cookie:
            return null_game.json()

        jwt = cherrypy.request.cookie[Helpers().get_cookie_name()]

        decoded = Helpers().decode_jwt(jwt.value)
        gameVerified = game.Verify.verify_game_by_id(decoded['gameId'])
        playerVerified = game.Verify.verify_player_in_game(decoded['gameId'], decoded['playerId'])
        
        if not gameVerified or not playerVerified:
            return null_game.json()
        
        created_game = viewmodels.JoinGameModel(decoded['gameId'], decoded['playerId'], decoded['key'])
        return created_game.json()
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def create(self):

        cherrypy.response.headers['Access-Control-Allow-Credentials'] = 'true'

        host_player_name = cherrypy.request.json['playerName']

        #create game
        created_game = game.CreateGame.create(host_player_name)

        #create cookie
        if not created_game.is_game_id_zero():
            jwt = Helpers().get_jwt(created_game.get_jwt_data())
            cherrypy.response.cookie[Helpers().get_cookie_name()] = jwt
            cherrypy.response.cookie[Helpers().get_cookie_name()]['expires'] = 7200

        return created_game.json()
