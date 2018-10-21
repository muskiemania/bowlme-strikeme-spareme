import bowl_game
from helpers import Helpers
from bowl_redis_dto import GameStatus

def handler(event, context):

    if 'headers' not in event.keys():
        return create_policy(event, False, {
            'gameIsVerified': 9,
            'playerIsVerified': 9,
            'playerIsHost': 9
        })

    if 'x-bowl-token' not in event['headers'].keys():
        return create_policy(event, False, {
            'gameIsVerified': 8,
            'playerIsVerified': 8,
            'playerIsHost': 8
        })

    jwt = event['headers']['x-bowl-token']

    decoded = Helpers().decode_jwt(jwt)

    game_id = 'gameId' in decoded.keys() and decoded['gameId'] or None
    player_id = 'playerId' in decoded.keys() and decoded['playerId'] or None
    key = 'key' in decoded.keys() and decoded['key'] or None

    if game_id is None or player_id is None:
        return create_policy(event, False, {
            'gameId': game_id or -1,
            'playerId': player_id or -2,
            'key': key or 'k'
        })

    game_statuses = [GameStatus.CREATED, GameStatus.STARTED]

    game_dto = bowl_game.Verify.verify_game_by_key(key)
    game_is_verified = game_dto.game_status in game_statuses
    player_is_verified = True #bowl_game.Verify.verify_player_in_game(key, player_id)

    return create_policy(event, game_is_verified and player_is_verified, {
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
            'Resource': 'arn:aws:execute-api:us-east-1:359299993558:ms9dw34ww0/*/GET/game'
        }]
    }

    auth_response['principalId'] = 'user'
    auth_response['policyDocument'] = policy_document
    auth_response['context'] = context

    return auth_response
