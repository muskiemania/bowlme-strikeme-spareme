import boto3
from boto3.dynamodb.types import TypeDeserializer
import json
import os


def handler(event, context):

    # first check http verb
    verb = event.get('requestContext', {}).get('http', {}).get('method')

    if verb == 'OPTIONS':
        return {
            'statusCode': 200, 
            'body': json.dumps({'message': 'OK'}), 
            'headers': {
                'Access-Control-Allow-Origin': '*', 
                'Access-Control-Allow-Headers': '*', 
                'Access-Control-Allow-Methods': 'OPTIONS, GET, POST', 
                'Content-Type': 'application/json'
            }
        }

    print(event)

    # must retrieve series from dynamodb
    '''
    {
        "series_id": "string",
        "games": ["string"],
        "game_data": {
            "string": {
                "frames: [ Object {
                    "number": "number",
                    "score": "number",
                    "total": "number",
                    "throws [ Object {
                        "pins": "string",
                        "id?": "string"
                    }],
                }],
                "analysis": { 
                    "string": { 
                        "raw": "string",
                        "url": "string
                    }
                }
            }
        }
    }
    '''
    _series_id = None

    if 'series_id' in event:
        _series_id = event.get('series_id')

    if 'pathParameters' in event:
        _series_id = event.get('pathParameters', {}).get('series_id')

    db = boto3.client('dynamodb')

    _metadata = json.loads(os.environ.get('DYNAMODB', {}))
    _table = _metadata.get('bowling-training-table', {})

    items = db.query(
        TableName=_table.get('table_name'),
        KeyConditionExpression='series_id = :series',
        ExpressionAttributeValues={
            ':series': {
                'S': _series_id
            }
        }
    )

    _i = items['Items']
    t = []
    dez = TypeDeserializer()
    for i in _i:
        t.append({k: TypeDeserializer().deserialize(v) for k, v in i.items()})

    s = {}
    s['series_id'] = _series_id
    s['games'] = []
    s['game_data'] = {}

    for g in t:
        _game_number = g.get('game_number')
        s['games'].append(_game_number)
        s['game_data'][str(_game_number)] = g

    print(s)

    return {
        'statusCode': 200,
        'body': json.dumps(s, default=str),
        'headers': {'Access-Control-Allow-Origin': '*'}
    }

