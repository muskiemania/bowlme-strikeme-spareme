
from common.socket import Socket

def handler(event, context):

    _detail = event.get('detail')
    
    _action = _detail.get('Action')
    _connection_id = _detail.get('Connection_Id')

    if _action != 'socket_disconnect':
        return

    Socket.disconnect(
            connection_id=_connection_id)

    return

