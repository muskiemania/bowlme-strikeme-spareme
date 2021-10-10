import traceback
import json
from bowl_game.score_hand import ScoreHand

def handler(event, context):

    # must fetch metadata from SNS
    _records = event.get('Records', [{}])
    for each in _records:
        _sns = each.get('Sns', {})
        _msg = json.loads(_sns.get('Message', '{}'))
    
    if not _msg:
        return

    print(_msg)

    _game_id = _msg.get('gameId')
    _player_id = _msg.get('playerId')
    _hand = _msg.get('hand')
    _status = _msg.get('status')
    _version = int(_msg.get('version'))

    if ScoreHand.score(_game_id, _player_id, _hand, _version, _status):
        return {
            'statusCode': 200,
            'body': 'OK'
        }

    return {
        'statusCode': 500,
        'body': f'unable to score hand for gameId: {_game_id}, playerId: {_player_id} and hand: {str(_hand)}'
    }

