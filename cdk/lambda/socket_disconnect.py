import os
import json
import boto3

def handler(event, context):

    # when a socket disconnects
    # need to remove the connection id from the players table

    # not going to do this synchronously
    # instead will publish an event to event bridge
    # and event bridge will handle it later

    _connection_id = event['requestContext']['connectionId']

    # need to send event to register user
    _event_metadata = json.loads(os.environ['EVENTBRIDGE'])
    _event_bus_name = _event_metadata.get('event_bus').get('event_bus_name')

    _events = boto3.client('events')
    _events.put_events(
            Entries=[
                {
                    'Detail': json.dumps({
                        'Action': 'socket_disconnect',
                        'Connection_Id': _connection_id}),
                    'DetailType': 'socket_disconnect',
                    'Source': 'bowlsocket.disconnect',
                    'EventBusName': _event_bus_name}])

    return {
        'statusCode': 200,
        'body': json.dumps({'msg': 'OK'})}

