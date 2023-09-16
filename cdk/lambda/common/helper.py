import boto3
import json
import os

class Helper:

    @staticmethod
    def get_host_id(**kwargs):
        _game_id = kwargs.get('game_id')

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')

        # then get the host from game
        _dynamo = boto3.client('dynamodb')
        reply = _dynamo.get_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id}},
                ConsistentRead=True,
                ProjectionExpression='#host',
                ExpressionAttributeNames={
                    '#host': 'Host_Id'})

        # must get host
        host = reply['Item']['Host_Id']['S']

        return host

    @staticmethod
    def get_player_hand(**kwargs):
        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')
        _rating = kwargs.get('rating')

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        # then get the players hand
        _dynamo = boto3.client('dynamodb')
        reply = _dynamo.get_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                ConsistentRead=True,
                ProjectionExpression='#hand',
                ExpressionAttributeNames={
                    '#hand': 'Hand'})


        # must get cards from player hand
        hand = reply['Item']['Hand']['L']
        cards = [c['S'] for c in hand]

        return cards

    @staticmethod
    def record_score(**kwargs):

        # need to get info from event
        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')
        _rating = kwargs.get('rating')

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _players_table_name = _table_metadata.get('players_table').get('table_name')

        # put new hand back to player
        _dynamo = boto3.client('dynamodb')
        reply = _dynamo.update_item(
                TableName=_players_table_name,
                Key={
                    'Game_Id': {
                        'S': _game_id},
                    'Player_Id': {
                        'S': _player_id}},
                UpdateExpression='SET #rating = :rating',
                ExpressionAttributeNames={
                    '#rating': 'Rating'},
                ExpressionAttributeValues={
                    ':rating': {'S': str(_rating)}})

        return

