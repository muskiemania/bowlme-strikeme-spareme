import cherrypy
import controllers

dispatcher = cherrypy.dispatch.RoutesDispatcher()

dispatcher.connect(name='api_create_game', route='/game/create', controller=controllers.CreateGameController(), action='index', conditions=dict(method=['GET']))
dispatcher.mapper.connect('/game/create', controller='api_create_game', action='create', conditions=dict(method=['POST']))

dispatcher.connect(name='api_get_game', route='/game/{game_id}/player/{player_id}', controller=controllers.GameController(), action='index', conditions=dict(method=['GET']))

dispatcher.connect(name='api_join_game', route='/game/join', controller=controllers.JoinGameController(), action='index', conditions=dict(method=['GET']))
dispatcher.mapper.connect('/game/join', controller='api_join_game', action='join', conditions=dict(method=['POST']))

dispatcher.connect(name='api_start_game', route='/game/start', controller=controllers.StartGameController(), action='index', conditions=dict(method=['GET']))
dispatcher.mapper.connect('/game/start', controller='api_start_game', action='start', conditions=dict(method=['POST']))


conf = {'/': {'request.dispatch': dispatcher}}
cherrypy.tree.mount(root=None, config=conf)

if hasattr(cherrypy.engine, 'block'):
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    cherrypy.server.quickstart()
    cherrypy.engine.start()
