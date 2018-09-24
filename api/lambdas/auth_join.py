import bowl_game
from helpers import Helpers
from bowl_redis_dto import GameStatus

def handler(event, context):

    if 'key' not in event.keys():
        return create_policy(event, False, {
            'gameIsVerified': False,
            'playerIsVerified': False,
            'playerIsHost': False
        })

    #jwt = event['headers']['X-Bowl-Token']

    #decoded = Helpers().decode_jwt(jwt)

    #game_id = 'gameId' in decoded.keys() and decoded['gameId'] or None
    #player_id = 'playerId' in decoded.keys() and decoded['playerId'] or None
    #key = 'key' in decoded.keys() and decoded['key'] or None

    #if game_id is None or player_id is None:
    #    return create_policy(event, False, {
    #        'gameId': 0,
    #        'playerId': 0,
    #        'key': None
    #    })

    game_statuses = [GameStatus.CREATED, GameStatus.STARTED]
    game_is_verified = bowl_game.Verify.verify_game_by_key(event['key'], game_statuses)

    return create_policy(event, game_is_verified, {
        'gameId': game_id,
        'playerId': player_id,
        'key': key
    })

def create_policy(event, effect, context):

    auth_response = {}

    policy_document = {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow' if effect else 'Deny',
            'Action': ['execute-api:Invoke'],
            'Resource': 'arn:aws:execute-api:us-east-1:359299993558:ms9dw34ww0/*/GET/*'
        }]
    }

    auth_response['principalId'] = 'user'
    auth_response['policyDocument'] = policy_document
    auth_response['context'] = context

    return auth_response
