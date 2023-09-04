import itertools
from random import randint
import boto3
import json
import os

class CreateDeck:

    @staticmethod
    def create(game_id, decks):

        cards = [str(x) for x in range(2,10)]
        cards += ['T', 'J', 'Q', 'K', 'A']

        suits = ['C', 'S', 'H', 'D']

        pairs = itertools.product(cards, suits)

        one_deck = [f'{card}{suit}' for (card, suit) in pairs]
        
        decks = one_deck * decks

        _table_metadata = json.loads(os.environ['DYNAMODB'])
        _games_table_name = _table_metadata.get('games_table').get('table_name')
 
        _dynamo = boto3.client('dynamodb')
        _dynamo.update_item(
                TableName=_games_table_name,
                Key={
                    'Game_Id': {
                        'S': game_id}},
                UpdateExpression='SET #deck = :deck, #discard = :discard',
                ExpressionAttributeNames={
                    '#deck': 'Deck',
                    '#discard': 'Discard'},
                ExpressionAttributeValues={
                    ':deck': {
                        'L': []},
                    ':discard': {
                        'L': [{'S': card} for card in decks]}})

        return
