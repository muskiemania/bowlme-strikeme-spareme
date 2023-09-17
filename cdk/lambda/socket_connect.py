import json
import boto3

def handler(event, context):

    # when a user connects there is no action to take

    return {
            'statusCode': 200,
            'body': json.dumps({'msg': 'OK'})}
