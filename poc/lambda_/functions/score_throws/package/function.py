import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
import itertools
import json
import os

from .helpers import new_calc_helper

def handler(event, context):

    # need series id and game number
    _series_id = event.get('series_id')
    _game_number = event.get('game_number')

    # get table name
    _metadata = json.loads(os.environ.get('DYNAMODB', {}))
    _table = _metadata.get('bowling-training-table', {})

    # retrieve all throws
    db = boto3.client('dynamodb')
    item = db.get_item(
        TableName=_table.get('table_name'),
        Key={
            'series_id': {'S': _series_id},
            'game_number': {'N': str(_game_number)}
        },
        ExpressionAttributeNames={
            '#data': 'throw_data'
        },
        ProjectionExpression='throws, #data'
    )

    data = item['Item']
    #print('query result is:')
    #print(data)
    dez = TypeDeserializer()
    th = dez.deserialize(data['throws'])
    print('th result is:')
    print(th)
    td = dez.deserialize(data['throw_data'])
    throws = [{'id': t, 'pins': td[t]['pins']} for t in th]
    
    
    for t in throws:
        if t['pins'] not in ['/', 'X']:
            t['pins'] = int(t['pins'])

    frames, score = new_calc_helper.calculate(throws)

    print(frames)
    print(score)

    '''
    frames is array of tuple of tuples
    [
        (
            (4, 'abc'), ('/', 'def')
        ),
        (
            ('4', 'xyz'), 
        )
    ]

    need to translate this to array of objects
    [
        {
            'frame': 1,
            'pins': 14,
            'total': 14,
            'throws': [
                {
                    'pins': '4',
                    'id': 'abc'
                },
                {
                    'pins': '/',
                    'id': 'def'
                }
            ]
         },
         {
            'frame': 2,
            'pins': 4,
            'total': 18,
            'throws: [
                {
                    'pins': '4',
                    'id': 'xyz'
                }
            ]
        }
     ]

    '''

    _FRAMES = [{'frame': i+1, 'throws': t} for i, t in enumerate(frames)]
    for i, s in enumerate(score):
        _FRAMES[i]['pins'] = s
    for i, s in enumerate(itertools.accumulate(score)):
        _FRAMES[i]['total'] = s

    for i in range(len(_FRAMES)):
        t = _FRAMES[i]['throws']
        print(f't is: {t}')
        _T = [{'pins': p, 'id': i} for (p, i) in list(t)]
        _FRAMES[i]['throws'] = _T

    sez = TypeSerializer()

    db.update_item(
        TableName=_table.get('table_name'),
        Key={
            'series_id': {'S': _series_id},
            'game_number': {'N': str(_game_number)}
        },
        UpdateExpression='SET #frames = :frames, #best = :best, #total = :total',
        ExpressionAttributeNames={
            '#frames': 'frames',
            '#best': 'best_possible',
            '#total': 'total'
        },
        ExpressionAttributeValues={
            ':frames': sez.serialize(_FRAMES),
            ':best': {
                'N': str(0)
            },
            ':total': {
                'N': str(list(itertools.accumulate(score))[-1])
            }
        }
    )

    return 'OK'

