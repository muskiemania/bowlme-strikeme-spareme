import traceback
import json
from bowl_game.shuffle_cards import ShuffleCards

def handler(event, context):

    # get game id from SNS
    _records = event.get('Records', [{}])
    for each in _records:
        _sns = each.get('Sns', {})
        _msg = json.loads(_sns.get('Message', '{}'))
        _body = _msg.get('body')

    if _body is None:
        return

    _body = json.loads(_body)
    _game_id = _body.get('gameId')

    if _game_id is None:
        return
   
    if ShuffleCards.shuffle(_game_id):
        return {
            'statusCode': 200,
            'body': 'OK'
        }

    return {
        'statusCode': 500,
        'body': f'unable to shuffle for gameId: {_game_id}'
    }

