import boto3
import json
import os
import uuid

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

    # step 1 create a unique id for the throw
    # step 2 write the throw
    # step 3 initialize the empty data map
    # step 4 add the data map

    # 1
    _id = str(uuid.uuid4()).split('-')[-1]

    # 2
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
                        'S': _id
                    }
                ]
            },
            ':empty': {
                'L': []
            }
        }
    )

    # 3

    # must make 2 more updates to initialize an empty data map
    # and then add the throw data to it

    try:
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
            UpdateExpression='SET #data = :empty',
            ConditionExpression='attribute_not_exists(#data)',
            ExpressionAttributeNames={
                '#data': 'throw_data',
            },
            ExpressionAttributeValues={
                ':empty': {
                    'M': {}
                }
            }
        )
    except:
        #this is stupid
        pass
       
    # 4
    _pins = ''
    _data = {}
    if 'throw' in event:
        _pins = event.get('throw')

        _data = {
            'pins': {'S': str(_pins)}
        }
    elif 'data' in event:
        if event.get('data', {}).get('pins') == 'X':
            _pins = 'X'
        elif event.get('data', {}).get('pins') == '/':
            _pins = '/'
        else:
            _pins = len(event.get('data', {}).get('pins'))

        _data = {
            'pins': {'S': str(_pins)},
            'raw': {'S': json.dumps(event.get('data'))}
        }

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
        UpdateExpression='SET #data.#id = :val',
        ExpressionAttributeNames={
            '#data': 'throw_data',
            '#id': _id
        },
        ExpressionAttributeValues={
            ':val': {
                'M': _data
            }
        }
    )
        
    return 'OK!'

