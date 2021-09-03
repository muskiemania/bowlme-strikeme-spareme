import boto3
from configs.dynamo import DynamoConfigs

class CreateGame:

    @staticmethod
    def create(game_id, cards):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.TABLE_NAME.value)

        table.put_item(
            Item={
                'game_id': game_id,
                'players': {},
                'game_status': 'created',
                'host_player_id': '',
                'deck': [],
                'discard': cards,
                'leaderboard': []
            }
        )

        return True
