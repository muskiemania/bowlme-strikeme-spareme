import boto3
from configs.dynamo import DynamoConfigs
import time

class CreatePlayer:

    @staticmethod
    def create(game_id, player_id, player_name, player_status, is_host=False):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.PLAYER_TABLE_NAME.value)

        # ttl ==> now + 4800
        _ttl = int(time.time()) + 4800

        table.put_item(
            Item={
                'game_id': game_id,
                'player_id': player_id,
                'player_name': player_name,
                'player_status': player_status,
                'hand': [],
                'score': ''
                'expires_at': _ttl
            }
        )

        return True
