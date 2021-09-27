import boto3
from configs.dynamo import DynamoConfigs
import time

class EmptyDiscard:

    @staticmethod
    def execute(game_id, cards):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.GAME_TABLE_NAME.value)

        # get version number
        _item = table.get_item(
            Key={
                'game_id': game_id,
                'pile_name': DynamoConfigs.DECK.value
            },
            ConsistentRead=True
        )

        version = _item.get('Item', {}).get('version', 0)

        if version == 0:
            raise Exception('unable to get version')

        # reset discard ->> [] and up version number
        # (conditional on matching previous)

        try:
            table.update_item(
                Key={
                    'game_id': game_id,
                    'pile_name': DynamoConfigs.DECK.value
                },
                UpdateExpression='SET #cards = list_append(#cards, :cards), version = :plusone'
                ConditionExpression='#version = :version',
                ExpressionAttributeNames={
                    '#cards': 'cards',
                    '#version': 'version'
                },
                ExpressionAttributeValues={
                    ':cards': cards,
                    ':plusone': version + 1,
                    ':version': version
                }
            )
        except:
            # conditional update failed
            raise
        else:
            # success!
            return True

