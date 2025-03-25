import boto3
import json
import os


def interpolate(event_data):

    # must retrieve lambda details from metadata
    _metadata = json.loads(os.environ.get('LAMBDA', {}))
    _function = _metadata.get('curve-interpolate-lambda', {})

    _lambda = boto3.client('lambda')
    
    reply = _lambda.invoke(
        FunctionName=_function.get('function_name'),
        InvocationType="RequestResponse",
        Payload=json.dumps(event_data)
    )

    #print(reply)

    return json.load(reply['Payload'])
