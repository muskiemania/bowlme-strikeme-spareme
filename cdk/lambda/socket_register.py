import uuid
import boto3
import time
import json
import os

from common.socket import Socket

def handler(event, context):

    _detail = event.get('detail')
    
    _action = _detail.get('Action')
    _game_id = _detail.get('Game_Id')
    _player_id = _detail.get('Player_Id')
    _connection_id = _detail.get('Connection_Id')

    if _action != 'socket_register':
        return

    Socket.register(
            game_id=_game_id, 
            player_id=_player_id, 
            connection_id=_connection_id)

    return

