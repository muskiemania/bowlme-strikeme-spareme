import cherrypy
import controllers

dispatcher = cherrypy.dispatch.RoutesDispatcher()

dispatcher.connect(name='api_health', route='/api/health', controller=controllers.HealthController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/health', controller='api_health', action='health', conditions=dict(method=['GET']))

dispatcher.connect(name='api_auth', route='/api/auth', controller=controllers.AuthorizeController(), action='index', conditions=dict(method=['GET']))
dispatcher.mapper.connect('/api/auth/game', controller='api_auth', action='verify_game', conditions=dict(method=['GET']))
dispatcher.mapper.connect('/api/auth/player', controller='api_auth', action='verify_player', conditions=dict(method=['GET']))

dispatcher.connect(name='api_create_game', route='/api/game/create', controller=controllers.CreateGameController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/create', controller='api_create_game', action='create', conditions=dict(method=['POST']))
dispatcher.mapper.connect('/api/game/create', controller='api_create_game', action='verify', conditions=dict(method=['GET']))

dispatcher.connect(name='api_join_game', route='/api/game/join', controller=controllers.JoinGameController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/join', controller='api_join_game', action='join', conditions=dict(method=['POST']))
dispatcher.mapper.connect('/api/game/join', controller='api_join_game', action='verify', conditions=dict(method=['GET']))

dispatcher.connect(name='api_get_game', route='/api/game', controller=controllers.GameController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game', controller='api_get_game', action='game', conditions=dict(method=['GET']))

dispatcher.connect(name='api_get_results', route='/api/results', controller=controllers.ResultsController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/results', controller='api_get_results', action='results', conditions=dict(method=['GET']))


dispatcher.connect(name='api_start_game', route='/api/game/start', controller=controllers.StartGameController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/start', controller='api_start_game', action='start', conditions=dict(method=['POST']))

dispatcher.connect(name='api_draw_cards', route='/api/game/draw', controller=controllers.DrawCardsController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/draw', controller='api_draw_cards', action='draw', conditions=dict(method=['POST']))

dispatcher.connect(name='api_discard_cards', route='/api/game/discard', controller=controllers.DiscardCardsController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/discard', controller='api_discard_cards', action='discard', conditions=dict(method=['POST']))

dispatcher.connect(name='api_finish_game', route='/api/game/finish', controller=controllers.FinishGameController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/finish', controller='api_finish_game', action='finish', conditions=dict(method=['POST']))

dispatcher.connect(name='api_end_game', route='/api/game/end', controller=controllers.EndGameController(), action='index', conditions=dict(method=['OPTIONS']))
dispatcher.mapper.connect('/api/game/end', controller='api_end_game', action='end', conditions=dict(method=['POST']))


conf = {}
conf['/'] = {'request.dispatch': dispatcher}

#grab environment vars from .env
env = {}
env_file = open('.env', 'r')
for line in env_file.read().splitlines():
    row = line.split('=')
    if len(row) == 2:
        env[row[0]] = row[1]

WEB_ORIGIN = env['WEB_ORIGIN']
API_PORT = int(env['API_PORT'])

cherrypy.config.update({'server.socket_port': API_PORT, 'tools.response_headers.on': True, 'tools.response_headers.headers': [('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', WEB_ORIGIN), ('Access-Control-Allow-Headers', 'Accept, Content-Type, X-Bowl-Token')]})

cherrypy.tree.mount(root=None, config=conf)

if hasattr(cherrypy.engine, 'block'):
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    cherrypy.server.quickstart()
    cherrypy.engine.start()
