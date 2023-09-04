import itertools
from random import randint
import boto3
import json
import os

class ShuffleDeck:

    @staticmethod
    def shuffle(game_id):

        # must set lock
        # get deck

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')
 
        _dynamo = boto3.client('dynamodb')
        reply = _dynamo.update_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': game_id}},
                UpdateExpression='SET #lock = :shuffling',
                ExpressionAttributeNames={
                    '#lock': 'Lock'},
                ExpressionAttributeValues={
                    ':locked': {
                        'S': 'locked'},
                    ':shuffling': {
                        'S': 'shuffling'}},
                ConditionExpression='attribute_not_exists(#lock) or #lock <> :locked')

        print(reply)

        game = _dynamo.get_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': game_id}},
                ProjectionExpression='Discard')

        cards = [c['S'] for c in game['Item']['Discard']['L']]

        for i in range(0, len(cards)-2):
            j = randint(i, len(cards)-1)
            cards[i], cards[j] = cards[j], cards[i]

        reply = _dynamo.update_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': game_id}},
                UpdateExpression='SET #deck = list_append(#deck, :deck), #discard = :discard, #lock = :unlocked',
                ExpressionAttributeNames={
                    '#deck': 'Deck',
                    '#discard': 'Discard',
                    '#lock': 'Lock'},
                ExpressionAttributeValues={
                    ':deck': {'L': [{'S': card} for card in cards]},
                    ':discard': {'L': []},
                    ':unlocked': {
                        'S': 'unlocked'},
                    ':shuffling': {'S': 'shuffling'}},
                ConditionExpression='#lock = :shuffling')

        return
