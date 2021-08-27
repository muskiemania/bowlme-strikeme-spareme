import boto3
from configs.dynamo import DynamoConfig

class CreateGame:

    @staticmethod
    def create(game_id, cards):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfig.TABLE_NAME)

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

        return True
