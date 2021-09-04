import boto3
from configs.dynamo import DynamoConfigs
import time

class CreateGame:

    @staticmethod
    def create(game_id, cards):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.TABLE_NAME.value)

        # ttl ==> now + 4800
        _ttl = int(time.time()) + 4800

        table.put_item(
            Item={
                'game_id': game_id,
                'players': {},
                'game_status': 'created',
                'host_player_id': '',
                'deck': [],
                'discard': cards,
                'leaderboard': [],
                'expires_at': _ttl
            }
        )

        return True
