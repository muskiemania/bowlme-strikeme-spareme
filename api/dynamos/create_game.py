import boto3
from configs.dynamo import DynamoConfigs
import time

class CreateGame:

    @staticmethod
    def create(game_id, cards):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.GAME_TABLE_NAME.value)

        # ttl ==> now + 4800
        _ttl = int(time.time()) + 4800

        table.put_item(
            Item={
                'game_id': game_id,
                'pile_name': str(DynamoConfigs.DECK.value),
                'cards': [],
                'version': 1,
                'expires_at': _ttl
            }
        )

        table.put_item(
            Item={
                'game_id': game_id,
                'pile': str(DynamoConfigs.DISCARD.value),
                'cards': cards,
                'version': 1,
                'expires_at': _ttl
            }
        )

        return True
