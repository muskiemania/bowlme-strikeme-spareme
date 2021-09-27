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
            Item={
                'game_id': game_id,
                'pile_name': str(DynamoConfigs.DECK.value)
            ),
            ConsistentRead=True
        )

        version = _item.get('version')

        # reset discard ->> [] and up version number
        # (conditional on matching previous)

        try:
            table.update_item(
                Item={
                    'game_id': game_id,
                    'pile_name': str(DynamoConfigs.DECK.value)
                },
                UpdateExpression='SET #cards = list_append(#cards, :cards), version = version + :one'
                ConditionExpression='version = :version',
                ExpressionAttributeNames={
                    '#cards': 'cards'
                },
                ExpressionAttributeValues={
                    ':cards': cards,
                    ':one': {'N': 1},
                    ':version': {'N': version}
                }
            )
        except:
            # conditional update failed
            raise
        else:
            # success!
            return True

