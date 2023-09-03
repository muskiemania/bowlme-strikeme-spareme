import uuid
import boto3
import time
import json
import os

class CreateGame:

    @staticmethod
    def execute(**kwargs):

        _game_id = str(uuid.uuid4())
        _player_name = kwargs.get('player_name')
        _player_id = str(uuid.uuid4())

        _decks = kwargs.get('decks', '1')

        try:
            _decks = int(_decks)
        except Exception as error:
            traceback.print_exc()
            raise error

        # ttl is now + 150min
        _ttl = int(time.time()) + 150 * 60

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        _dynamo = boto3.client('dynamodb')
        _dynamo.batch_write_item(
                RequestItems={
                    _games_table_name: [
                        {
                            'PutRequest': {
                                'Item': {
                                    'Game_Id': {
                                        'S': _game_id},
                                    'Host_Id': {
                                        'S': _player_id},
                                    'TTL': {
                                        'N': str(_ttl)}
                                    }
                                }
                            }
                        ],
                    _players_table_name: [
                        {
                            'PutRequest': {
                                'Item': {
                                    'Game_Id': {
                                        'S': _game_id},
                                    'Player_Id': {
                                        'S': _player_id},
                                    'TTL': {
                                        'N': str(_ttl)}
                                    }
                                }
                            }
                        ]
                    })
                    
        # need to send event to create deck

        _event_metadata = json.loads(os.environ['EVENTBRIDGE'])
        _event_bus_name = _event_metadata.get('event_bus').get('event_bus_name')

        _events = boto3.client('events')
        _events.put_events(
                Entries=[
                    {
                        'Detail': json.dumps({
                            'Action': 'create_deck',
                            'Game_Id': _game_id}),
                        'DetailType': 'create a deck',
                        'Source': 'bowlapi.create_game',
                        'EventBusName': _event_bus_name}])

        # need to return enough info to generate a token
        return {
                'game_id': _game_id,
                'player_id': _player_id,
                'player_name': _player_name,
                'ttl': _ttl}
