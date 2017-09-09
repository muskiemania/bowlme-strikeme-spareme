import cherrypy
import json
import game

class DrawCardsController(object):

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
    def draw(self):
        game_id = cherrypy.request.json['gameId']
        player_id = cherrypy.request.json['playerId']
        number_of_cards = cherrypy.request.json['numberOfCards'] or 1
        return game.DrawCards.draw(game_id, player_id, number_of_cards).json()
