import traceback
import json
from bowl_game.score_hand import ScoreHand

def handler(event, context):

    # must fetch metadata from SNS
    _records = event.get('Records', [{}])
    for each in _records:
        _sns = each.get('Sns', {})
        _msg = json.loads(_sns.get('Message', '{}')
    
    if not _msg:
        return

    _game_id = _msg.get('gameId')
    _player_id = _msg.get('playerId')
    _hand = _msg.get('cards')

    if ScoreHand.score(_game_id, _player_id, _hand):
        return {
            'statusCode': 200,
            'body': 'OK'
        }

    return {
        'statusCode': 500,
        'body': f'unable to score hand for gameId: {_game_id}, playerId: {_player_id} and hand: {str(_hand)}'
    }

