import uuid
import boto3
import time
import json
import os

class GameStatus:

    @staticmethod
    def start(**kwargs):

        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')

        # need to check to make sure the host is starting game

        #_table_metadata = json.loads(os.environ['DYNAMODB'])
        #_games_table_name = _table_metadata.get('games_table').get('table_name')

        # need to send event to shuffle deck

        _event_metadata = json.loads(os.environ['EVENTBRIDGE'])
        _event_bus_name = _event_metadata.get('event_bus').get('event_bus_name')

        _events = boto3.client('events')
        _events.put_events(
                Entries=[
                    {
                        'Detail': json.dumps({
                            'Action': 'shuffle_deck',
                            'Game_Id': _game_id}),
                        'DetailType': 'shuffle deck',
                        'Source': 'bowlapi.game_status.start',
                        'EventBusName': _event_bus_name}])

        return
