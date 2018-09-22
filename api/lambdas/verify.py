import bowl_game
from .helpers import Helpers
from bowl_redis_dto import GameStatus

def handler(event, context):

    jwt = event['headers']['X-Bowl-Token']

    decoded = Helpers().decode_jwt(jwt)

    game_id = decoded['gameId'] #cherrypy.request.cookie['game_auth']
    player_id = decoded['playerId'] #cherrypy.request.cookie['player_auth']

    game_verified = bowl_game.Verify.verify_game_by_id(game_id, [GameStatus.CREATED])
    player_verified = bowl_game.Verify.verify_player_in_game(game_id, player_id)
    player_is_host = bowl_game.Verify.verify_player_is_host(game_id, player_id)

    auth_response = {}

    policy_document = {
        'Version': 'version',
        'Statement': [{
            'Sid': 'asd',
            'Action': 'asd',
            'Effect': 'asd',
            'Resource': 'asd'
        }]
    }

    auth_response['policyDocument'] = policy_document

    return auth_response
