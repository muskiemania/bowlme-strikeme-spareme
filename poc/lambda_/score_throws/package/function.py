import boto3
import itertools
import json
import os

from .helpers import calc_helper

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
        ProjectionExpression='throws'
    )

    throws = item['Item'].get('throws', {}).get('L', [])
    throws = [t.get('M', {}).get('pins_result', {}).get('S') for t in throws]
    throws = [(lambda x: x if x in ['/', 'X'] else int(x))(t) for t in throws]

    print(throws)

    frames, score = calc_helper.calculate(throws)

    print(frames)
    print(score)

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
            ':frames': {
                'L': [
                    {
                        'M': {
                            'frame_number': {
                                'S': str(i + 1)
                            },
                            'score': {
                                'N': str(score[i])
                            },
                            'throws': {
                                'L': [
                                    {
                                        'S': str(t)
                                    } for t in list(f)
                                ]
                            }
                        }
                    } for i, f in enumerate(frames)
                ]
            },
            ':best': {
                'N': str(0)
            },
            ':total': {
                'N': str(list(itertools.accumulate(score))[-1])
            }
        }
    )

    return 'OK'
