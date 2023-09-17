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

    @staticmethod
    def disconnect(**kwargs):

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _players_table_name = _table_metadata.get('players_table').get('table_name')
        _socket_index_name = _table_metadata.get('socket_index').get('index_name')

        _connection_id = kwargs.get('connection_id')

        _dynamo = boto3.client('dynamodb')
        items = _dynamo.query(
                TableName=_players_table_name,
                IndexName=_socket_index_name,
                ExpressionAttributeNames={
                    '#connectionid': 'Connection_Id'},
                ExpressionAttributeValues={
                    ':connectionid': {'S': _connection_id}},
                KeyConditionExpression='#connectionid = :connectionid')
        
        rows_to_delete = [(i['Game_Id']['S'], i['Player_Id']['S']) for i in items['Items']]

        for (_game_id, _player_id) in rows_to_delete:
            _dynamo.update_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                UpdateExpression='REMOVE #connectionid',
                ExpressionAttributeNames={
                    '#connectionid': 'Connection_Id'})

        return 'OK'


