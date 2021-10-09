import boto3
from configs.dynamo import DynamoConfigs
import time

class DrawCards:

    @staticmethod
    def execute(game_id, player_id, number_of_cards):
        
        db = boto3.resource('dynamodb')

        # get deck + version number
        table = db.Table(DynamoConfigs.GAME_TABLE_NAME.value)
        _item = table.get_item(
            Key={
                'game_id': game_id,
                'pile_name': DynamoConfigs.DECK.value
            },
            ConsistentRead=True
        )

        deck_version = _item.get('Item', {}).get('version', 0)
        deck_cards = _item.get('Item', {}).get('cards', [])

        if deck_version == 0 or len(deck_cards) == 0:
            raise Exception('unable to fetch cards and version')

        if number_of_cards > len(deck_cards):
            raise Exception('not enough cards on the deck to draw')

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
        player_cards = _item.get('Item', {}).get('cards', [])

        if player_version == 0:
            raise Exception('unable to fetch player version')

        # now need to prepare data to write

        drawn = deck_cards[:number_of_cards]
        deck = deck_cards[number_of_cards:]

        client = boto3.client('dynamodb')
        
        try:
            response = client.transact_write_items(
                TransactItems=[{
                    'Update': {
                        'Key': {
                            'game_id': game_id,
                            'pile_name': DynamoConfigs.DECK.value
                        }
                    },
                    'UpdateExpression': 'SET #cards = :cards, #version = :plusone',
                    'TableName': DynamoConfigs.GAME_TABLE_NAME.value,
                    'ConditionExpression': '#version = :version',
                    'ExpressionAttributeNames': {
                        '#cards': 'cards',
                        '#version': 'version'
                    },
                    'ExpressionAttributeValues': {
                        ':cards': deck,
                        ':plusone': deck_version + 1,
                        ':version': deck_version
                    }
                }, {
                    'Update': {
                        'Key': {
                            'game_id': game_id,
                            'player_id': player_id
                        }
                    },
                    'UpdateExpression': 'SET #hand = list_append(#hand, :cards), #version = :plusone',
                    'TableName': DynamoConfigs.PLAYER_TABLE_NAME.value,
                    'ConditionExpression': '#version = :version',
                    'ExpressionAttributeNames': {
                        '#hand': 'hand',
                        '#version': 'version'
                    },
                    'ExpressionAttributeValues': {
                        ':cards': drawn,
                        ':plusone': player_version + 1,
                        ':version': player_version
                    }
                }]
            )
        except:
            # some kind of transaction error
        else:
            # success!
            _hand = []
            _hand.extend(player_hand)
            _hand.extend(drawn)
            return (_hand, player_version + 1, len(deck))

