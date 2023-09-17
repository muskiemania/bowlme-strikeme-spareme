import os
import json
import boto3

def handler(event, context):

    # when a socket sends a message
    # need to do something
    # will figure out what to do here
    # but will handle the rest asynchronously

    _body = json.loads(event.get('body', ''))
    #_route_key = event['requestContext']['routeKey']
    _connection_id = event['requestContext']['connectionId']
    _action = _body.get('action')

    if _action == 'register':
        # register: takes game id + player id + connection id
        # and appends the connection id to the row in players table

        _game_id = _body.get('gameId')
        _player_id = _body.get('playerId')

        # need to send event to register user
        _event_metadata = json.loads(os.environ['EVENTBRIDGE'])
        _event_bus_name = _event_metadata.get('event_bus').get('event_bus_name')

        _events = boto3.client('events')
        _events.put_events(
                Entries=[
                    {
                        'Detail': json.dumps({
                            'Action': 'socket_register',
                            'Game_Id': _game_id,
                            'Player_Id': _player_id,
                            'Connection_Id': _connection_id}),
                        'DetailType': 'socket_register',
                        'Source': 'bowlsocket.register',
                        'EventBusName': _event_bus_name}])

        #    if _route key == 'finish':
        # finish: flags the user as no longer drawing any more cards
        # needs to see leaderboard updates based upon others
        #pass

    return {
        'statusCode': 200,
        'body': json.dumps({'msg': 'OK'})}

