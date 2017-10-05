import cherrypy
import json
import game
import viewmodels
from . import Helpers

class JoinGameController(object):

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
    def join(self):

        game_key = cherrypy.request.json['gameKey']
        player_name = cherrypy.request.json['playerName']

        #join game
        joined_game = game.JoinGame(game_key)
        reply = joined_game.execute(player_name)

        #create cookie
        if not reply.is_game_id_zero():
            jwt = Helpers().get_jwt(reply.get_jwt_data())
            cherrypy.response.cookie[Helpers().get_cookie_name()] = jwt
            cherrypy.response.cookie[Helpers().get_cookie_name()]['expires'] = 7200

        return reply.json()
