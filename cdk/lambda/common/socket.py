import os
import json
import boto3

class Socket:

    @staticmethod
    def register(**kwargs):

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')
        _connection_id = kwargs.get('connection_id')

        _dynamo = boto3.client('dynamodb')
        _dynamo.update_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                UpdateExpression='SET #connectionid = :connectionid',
                ExpressionAttributeNames={
                    '#connectionid': 'Connection_Id'},
                ExpressionAttributeValues={
                    ':connectionid': {'S': _connection_id}})

        return 'OK'
