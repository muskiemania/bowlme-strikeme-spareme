import uuid
import boto3
import time
import json
import os

class JoinGame:

    @staticmethod
    def execute(**kwargs):

        _game_id = kwargs.get('game_id')
        _player_name = kwargs.get('player_name')
        _player_id = str(uuid.uuid4())

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        _dynamo = boto3.client('dynamodb')
        response = _dynamo.get_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id}},
                ProjectionExpression='#ttl',
                ExpressionAttributeNames={
                    '#ttl': 'TTL'})

        if 'Item' not in response:
            return

        _ttl = response['Item']['TTL']['N']
                    
        _dynamo.put_item(
                TableName=_players_table_name,
                Item={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id},
                    'Player_Name': {
                        'S': _player_name},
                    'TTL': {
                        'N': str(_ttl)}})

        # need to return enough info to generate a token
        return {
                'game_id': _game_id,
                'player_id': _player_id,
                'player_name': _player_name,
                'ttl': _ttl}
