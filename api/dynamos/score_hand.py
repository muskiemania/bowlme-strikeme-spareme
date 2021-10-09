import boto3
from configs.dynamo import DynamoConfigs
import time

class ScoreHand:

    @staticmethod
    def execute(game_id, player_id, rating, version, status):
        
        db = boto3.resource('dynamodb')

        # write rating and status
        table = db.Table(DynamoConfigs.PLAYER_TABLE_NAME.value)
        try:
            _item = table.update_item(
                Key={
                    'game_id': game_id,
                    'player_id': player_id
                },
                UpdateExpression='SET #score = :score, #status = :status, #version = :plusone',
                ConditionExpression='#version = :version',
                ExpressionAttributeNames={
                    '#score': 'score',
                    '#status': 'status',
                    '#version': 'version'
                },
                ExpressionAttributeValues={
                    ':score': rating,
                    ':status': status,
                    ':plusone': version + 1,
                    ':version': version
                }
            )
        except:
            raise
        else:
            return True

