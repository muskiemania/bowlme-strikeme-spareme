import bowl_game
from helpers import Helpers
from bowl_redis_dto import GameStatus

def handler(event, context):

    if 'headers' not in event.keys():
        return create_policy(event, {
            'gameIsVerified': False,
            'playerIsVerified': False,
            'playerIsHost': False
        })

    if 'X-Bowl-Token' not in event['headers'].keys():
        return create_policy(event, {
            'gameIsVerified': False,
            'playerIsVerified': False,
            'playerIsHost': False
        })

    jwt = event['headers']['X-Bowl-Token']

    decoded = Helpers().decode_jwt(jwt)

    game_id = 'gameId' in decoded.keys() and decoded['gameId'] or None
    player_id = 'playerId' in decoded.keys() and decoded['playerId'] or None
    key = 'key' in decoded.keys() and decoded['key'] or None

    if game_id is None or player_id is None:
        return create_policy(event, {
            'gameIsVerified': False,
            'playerIsVerified': False,
            'playerIsHost': False
        })

    game_statuses = [GameStatus.CREATED, GameStatus.STARTED]

    game_is_verified = bowl_game.Verify.verify_game_by_id(game_id, game_statuses)
    player_is_verified = bowl_game.Verify.verify_player_in_game(game_id, player_id)
    player_is_host = bowl_game.Verify.verify_player_is_host(game_id, player_id)

    return create_policy(event, {
        'gameIsVerified': game_is_verified,
        'playerIsVerified': player_is_verified,
        'playerIsHost': player_is_host,
        'gameId': game_id,
        'playerId': player_id,
        'key': key
    })

def create_policy(event, context):

    auth_response = {}

    policy_document = {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': ['execute-api:Invoke'],
            'Resource': 'arn:aws:execute-api:us-east-1:359299993558:ms9dw34ww0/*/GET/*'
        }]
    }

    auth_response['principalId'] = 'user'
    auth_response['policyDocument'] = policy_document
    auth_response['context'] = context

    return auth_response
