import boto3
from configs.dynamo import DynamoConfigs
import time

class CreatePlayer:

    @staticmethod
    def create(game_id, player_id, player_name, player_status, is_host=False):
        
        db = boto3.resource('dynamodb')
        table = db.Table(DynamoConfigs.TABLE_NAME.value)

        _player = {
            'player_name': player_name,
            'hand': [],
            'score': '',
            'status': player_status,
            'player_id': player_id
        }

        _update_expression = f'set #players.#player_id = :player'
        _expression_names = {
            '#players': 'players',
            '#player_id': player_id
        }
        _expression_values = {
            ':player': _player
        }

        if is_host:
            _update_expression += ', host_player_id = :player_id'
            _expression_values[':player_id'] = player_id

        table.update_item(
            Key={
                'game_id': game_id
            },
            UpdateExpression=_update_expression,
            ExpressionAttributeNames=_expression_names,
            ExpressionAttributeValues=_expression_values
        )

        return True
