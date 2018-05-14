import cherrypy
import json

class HealthController(object):

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET'
        return json.dumps({'ok': True})

    @cherrypy.expose
    def health(self):

        response = {'hello': 'there'}

        return json.dumps(response)
