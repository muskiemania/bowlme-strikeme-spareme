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
            Item={
                'game_id': game_id,
                'pile_name': str(DynamoConfigs.DISCARD.value)
            ),
            ConsistemtRead=True
        )

        version = _item.get('version')
        cards = item.get('cards')

        # reset discard ->> [] and up version number
        # (conditional on matching previous)

        try:
            table.update_item(
                Item={
                    'game_id': game_id,
                    'pile_name': str(DynamoConfigs.DISCARD.value)
                },
                UpdateExpression='SET cards = :cards, version = version + :one',
                ConditionExpression='version = :version',
                ExpressionAttributeVaues={
                    ':cards': [],
                    ':one': {'N': 1},
                    ':version': {'N': version}
                }
            )
        except:
            # conditional update failed
            raise
        else:
            # success!
            return cards

