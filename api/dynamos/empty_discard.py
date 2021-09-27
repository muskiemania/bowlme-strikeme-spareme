import boto3
from configs.dynamo import DynamoConfigs
import time

class EmptyDiscard:

    @staticmethod
    def execute(game_id):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.GAME_TABLE_NAME.value)

        # get discard + version number
        _item = table.get_item(
            Key={
                'game_id': game_id,
                'pile_name': DynamoConfigs.DISCARD.value
            },
            ConsistentRead=True
        )

        version = _item.get('Item', {}).get('version', 0)
        cards = _item.get('Item', {}).get('cards', [])

        if version == 0 or len(cards) == 0:
            raise Exception('unable to fetch cards and version')

        # reset discard ->> [] and up version number
        # (conditional on matching previous)

        try:
            table.update_item(
                Key={
                    'game_id': game_id,
                    'pile_name': DynamoConfigs.DISCARD.value
                },
                UpdateExpression='SET #cards = :cards, #version = :plusone',
                ConditionExpression='#version = :version',
                ExpressionAttributeNames={
                    '#cards': 'cards',
                    '#version': 'version'
                },
                ExpressionAttributeValues={
                    ':cards': [],
                    ':plusone': version + 1,
                    ':version': version
                }
            )
        except:
            # conditional update failed
            raise
        else:
            # success!
            return cards

