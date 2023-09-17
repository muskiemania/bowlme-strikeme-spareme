import boto3

def handler(event, context):

    # when a socket disconnects
    # need to remove the connection id from the players table

    # not going to do this synchronously
    # instead will publish an event to event bridge
    # and event bridge will handle it later

    return 'OK'
