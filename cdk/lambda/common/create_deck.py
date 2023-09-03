import itertools
from random import randint
import boto3

class CreateDeck:

    @staticmethod
    def create(game_id, decks):

        cards = [str(x) for x in range(2,10)]
        cards += ['T', 'J', 'Q', 'K', 'A']

        suits = ['C', 'S', 'H', 'D']

        pairs = itertools.product(cards, suits)

        one_deck = [f'{c}{s}' for (card, suit) in pairs]
        
        decks = one_deck * decks

        _dynamo = boto3.client('dynamodb')
        _dynamo.update_item(
                TableName='',
                Key='Game_Id': {
                    'S': game_id},
                UpdateExpression='SET #discard = :discard',
                ExpressionAttributeNames={
                    '#discard': 'Discard'},
                ExpressionAttributeValues={
                    ':discard': {
                        'L': decks }})

        return
