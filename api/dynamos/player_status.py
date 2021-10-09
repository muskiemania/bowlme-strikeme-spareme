import boto3
from configs.dynamo import DynamoConfigs
import time

class PlayerStatus:

    @staticmethod
    def _status(game_id, player_id, status, conditional=None):

        _condition_expression = None
        _expression_attribute_values = {
            ':status': status,
        }

        if conditional is not None:
            _condition_expression = '#status = :old_status'
            _expression_attribute_values[':old_status'] = conditional
         
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.PLAYER_TABLE_NAME.value)

        try:
            table.update_item(
                Key={
                    'game_id': game_id,
                    'player_id': player_id
                },
                UpdateExpression='SET #status = :status, #version = #version + 1',
                ConditionExpression=_condition_expression,
                ExpressionAttributeNames={
                    '#status': 'player_status',
                    '#version': 'version'
                },
                ExpressionAttributeValues=_expression_attribute_values
            )
        except:
            # conditional update failed
            raise
        else:
            # success!
            return True

    @staticmethod
    def must_discard(game_id, player_id, to_finished=False):
    
        if to_finished:
            return PlayerStatus._status(game_id, player_id, DynamoConfigs.FINISHED_MUST_DISCARD.value, DynamoConfigs.DEALT.value)

        return PlayerStatus._status(game_id, player_id, DynamoConfigs.MUST_DISCARD.value, DynamoConfigs.DEALT.value)

    @staticmethod
    def dealt(game_id, player_id):

        return PlayerStatus._status(game_id, player_id, DynamoConfigs.DEALT.value)
            
    @staticmethod
    def finished(game_id, player_id):

        return PlayerStatus._status(game_id, player_id, DynamoConfigs.FINISHED.value)
