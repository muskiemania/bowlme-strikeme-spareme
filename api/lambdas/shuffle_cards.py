import traceback
import json
from bowl_game.shuffle_cards import ShuffleCards

def handler(event, context):
    # fetch input
    _body = event.get('body')
    _body = json.loads(_body)

    # get game id from SNS
    _game_id = ''
   
    if ShuffleCards.shuffle(_game_id):
        return {
            'statusCode': 200,
            'body': 'OK'
        }

    return {
        'statusCode': 500,
        'body': f'unable to shuffle for gameId: {_game_id}'
    }

