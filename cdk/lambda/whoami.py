import json
import traceback

def handler(event, context):

    try:
        _auth_context = event.get('requestContext', {}).get('authorizer', {}).get('lambda', {})
        
        _game_id = _auth_context['gameId']
        _player_id = _auth_context['playerId']
        _player_name = _auth_context['playerName']
    except:
        traceback.print_exc()

    return {
            'statusCode': 200,
            'body': json.dumps({
                'gameId': _game_id,
                'playerId': _player_id,
                'playerName': _player_name})}

