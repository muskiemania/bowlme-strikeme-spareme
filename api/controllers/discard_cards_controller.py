import cherrypy
import json
import game

class DiscardCardsController(object):

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
    def discard(self):
        game_id = cherrypy.request.json['gameId']
        player_id = cherrypy.request.json['playerId']
        discard_cards = cherrypy.request.json['discardCards']
        return game.DiscardCards.discard(game_id, player_id, discard_cards).json()
