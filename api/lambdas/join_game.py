import traceback
import json
from bowl_game.join_game import JoinGame

def handler(event, context):
    # fetch input
    _body = event.get('body')
    _body = json.loads(_body)

    _host_player_name = _body.get('hostPlayerName', 'Anonymous')
   
    _game_id = body.get('gameId')
    _player_name = body.get('playerName')
    _is_host = False

    if _game_id is None or _player_name is None:
        return {
            'statusCode': 500,
            'body': 'gameId and playerName are required'
        }
    
    _player_id = JoinGame.join(_game_id, _player_name, _is_host)
    
    # return player info
    return {
        'statusCode': 200,
        'body': json.dumps({
            'gameId': _game_id,
            'playerId': _player_id
        })
    }


'''

import bowl_game
from helpers import Helpers

def handler(event, context):

    game_key = 'key' in event.keys() and event['key'] or None
    player_name = 'playerName' in event.keys() and event['playerName'] or None

    #join game
    join_game = bowl_game.JoinGame(game_key)
    joined_game = join_game.execute(player_name)

    #create cookie
    if not joined_game.is_game_id_zero():
        jwt = Helpers().get_jwt(joined_game.get_jwt_data())
        joined_game.set_jwt(jwt)

    return joined_game.json()

'''
