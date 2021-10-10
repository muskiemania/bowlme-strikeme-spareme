import boto3
from configs.dynamo import DynamoConfigs
from configs.player_status import PlayerStatusConfigs
import time

class DiscardCards:

    @staticmethod
    def execute(game_id, player_id, cards):
        
        db = boto3.resource('dynamodb')

        # get deck + version number
        table = db.Table(DynamoConfigs.GAME_TABLE_NAME.value)
        _item = table.get_item(
            Key={
                'game_id': game_id,
                'pile_name': DynamoConfigs.DISCARD.value
            },
            ConsistentRead=True
        )

        discard_version = _item.get('Item', {}).get('version', 0)

        if discard_version == 0:
            raise Exception('unable to fetch discard and version')

        # get player hand + version number
        table = db.Table(DynamoConfigs.PLAYER_TABLE_NAME.value)
        _item = table.get_item(
            Key={
                'game_id': game_id,
                'player_id': player_id
            },
            ConsistentRead=True
        )

        player_version = _item.get('Item', {}).get('version', 0)
        player_cards = _item.get('Item', {}).get('hand', [])
        player_status = _item.get('Item', {}).get('status')

        if player_version == 0:
            raise Exception('unable to fetch player version')

        if player_status in [PlayerStatusConfigs.JOINED.value, PlayerStatusConfigs.FINISHED.value]:
            raise Exception(f'cannot discard cards for player with status {player_status}')

        # make sure player has the cards they are discarding...
        to_discard = []
        while cards:
            _a_card = cards.pop()
            if _a_card not in player_cards:
                raise Exception(f'cannot discard {_a_card} because player doesnt have it')
            player_cards.remove(_a_card)
            to_discard.append(_a_card)

        # now need to prepare data to write

        client = boto3.client('dynamodb')
        
        try:
            response = client.transact_write_items(
                TransactItems=[{
                    'Update': {
                        'Key': {
                            'game_id': {'S': game_id},
                            'pile_name': {'S': DynamoConfigs.DISCARD.value}
                        },
                        'UpdateExpression': 'SET #cards = list_append(#cards, :discards), #version = :plusone',
                        'TableName': DynamoConfigs.GAME_TABLE_NAME.value,
                        'ConditionExpression': '#version = :version',
                        'ExpressionAttributeNames': {
                            '#cards': 'cards',
                            '#version': 'version'
                        },
                        'ExpressionAttributeValues': {
                            ':discards': {'L': [{'S': card} for card in to_discard]},
                            ':plusone': {'N': str(discard_version + 1)},
                            ':version': {'N': str(discard_version)}
                        }
                    }
                }, {
                    'Update': {
                        'Key': {
                            'game_id': {'S': game_id},
                            'player_id': {'S': player_id}
                        },
                        'UpdateExpression': 'SET #hand = :discarded, #version = :plusone',
                        'TableName': DynamoConfigs.PLAYER_TABLE_NAME.value,
                        'ConditionExpression': '#version = :version',
                        'ExpressionAttributeNames': {
                            '#hand': 'hand',
                            '#version': 'version'
                        },
                        'ExpressionAttributeValues': {
                            ':discarded': {'L': [{'S': card} for card in player_cards]},
                            ':plusone': {'N': str(player_version + 1)},
                            ':version': {'N': str(player_version)}
                        }
                    }
                }]
            )
        except:
            # some kind of transaction error
            raise
        else:
            # success!
            return (player_cards, player_version + 1, player_status)

