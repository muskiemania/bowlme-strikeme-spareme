import boto3
import json
import os

def handler(event, context):

    # important data points from input are:
    # series id
    # game_num
    # throw / throw_data
    '''
    {
        "series_id": "string",
        "game_num": "number",
        "throw?": "string"
        "data?": "Object" {
            "ball?": "string",
            "start_distance?": "number (15|12)"
            "start?": "number (1-39)",
            "slide?": "number (1-39)",
            "arrows?": "number (1-39)",
            "break_point?": "number (1-39)",
            "break_distance?": "number (34-60)"
            "pin_entry?": "number (1-39)",
            "pin_exit?": "number (1-39)",
            "pins?"; [ "number" ]
        }
    }
    '''

    _series_id = event.get('series_id')
    _game_number = event.get('game_number')

    if 'throw' in event:

        # put only the throw into dynamo db and then return
        db = boto3.client('dynamodb')

        _metadata = json.loads(os.environ.get('DYNAMODB', {}))
        _table = _metadata.get('bowling-training-table', {})

        db.update_item(
            TableName=_table.get('table_name'),
            Key={
                'series_id': {
                    'S': _series_id
                 },
                'game_number': {
                    'N': str(_game_number)
                }
            },
            UpdateExpression='SET #throws = list_append(if_not_exists(#throws, :empty), :thr)',
            ExpressionAttributeNames={
                '#throws': 'throws'
            },
            ExpressionAttributeValues={
                ':thr': {
                    'L': [
                        {
                            'M': {
                                'pins_result': {
                                    'S': event.get('throw')
                                }
                            }
                        }
                    ]
                },
                ':empty': {
                    'L': []
                }
            }
        )

        return 'OK'

    if 'data' in event:

        # put the data into dynamodb and then return
        
        return 'OK!'

