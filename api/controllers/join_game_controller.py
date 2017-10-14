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

        x_header = cherrypy.serving.request.headers['X-Bowl-Token'] or ''
        
        if x_header == '' or x_header == 'undefined': 
            return null_game.json()

        decoded = Helpers().decode_jwt(x_header)
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
        join_game = game.JoinGame(game_key)
        joined_game = join_game.execute(player_name)

        #create cookie
        if not joined_game.is_game_id_zero():
            jwt = Helpers().get_jwt(joined_game.get_jwt_data())
            joined_game.set_jwt(jwt)

        return joined_game.json()
