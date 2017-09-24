import cherrypy
import json
import game
from . import Helpers

class JoinGameController(object):

    def __init__(self):
        pass
    
    @cherrypy.config(**{'tools.response_headers.on': True, 'tools.response_headers.headers': [('Content-Language', 'en-US'), ('Content-Type', 'application/json')]})

    @cherrypy.expose
    def index(self):

        #try:
        cookie_value = cherrypy.request.cookie[Helpers().get_cookie_name()].value
        decoded = Helpers().decode_jwt(cookie_value)
        print decoded
        join_game = game.JoinGame(game_id=decoded['gameId'])
        joined_game = join_game.execute(player_id=decoded['playerId'])

        return joined_game.json()
        #except Exception as e:
        #    return json.dumps({ 'gameId': 0, 'playerId': 0, 'error': str(e) })

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def join(self):

        #input is: a key abcdef, and a player name
        #processing is: verify that the game exists. if so then join game.
        #output is: game_id and player_id
        
        game_key = cherrypy.request.json['gameKey']
        player_name = cherrypy.request.json['playerName']

        join_game = game.JoinGame(game_key=game_key)
        joined_game = join_game.execute(player_name=player_name)

        if joined_game.game_id != 0:
            jwt = Helpers().get_jwt(joined_game.get_jwt_data())
            cherrypy.response.cookie[Helpers().get_cookie_name()] = jwt
            cherrypy.response.cookie[Helpers().get_cookie_name()]['expires'] = 7200

        return joined_game.json()
