import json
from common.game_status import GameStatus
from common.helper import Helper

def handler(event, context):


    try:
        _auth_context = event.get('requestContext', {}).get('authorizer', {}).get('lambda', {})
        
        _game_id = _auth_context['gameId']
        _player_id = _auth_context['playerId']
    except:
        traceback.print_exc()

    _body = json.loads(event.get('body'))
    _status = _body.get('status')

    if _status == 'start':
        _host = Helper.get_host_id(
                game_id=_game_id)

        if _player_id != _host:
            return {
                    'statusCode': 400,
                    'body': json.dumps('failed')}

        GameStatus.start(
                game_id=_game_id,
                player_id=_player_id)

        return {
                'statusCode': 200,
                'body': json.dumps('OK')}
