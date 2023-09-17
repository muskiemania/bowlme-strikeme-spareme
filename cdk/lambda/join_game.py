import json

from common.join_game import JoinGame
from common.auth_token import AuthToken

def handler(event, context):

    # get player name from event
    # get number of decks from event

    _body = json.loads(event.get('body'))

    _player_name = _body.get('playerName')
    _game_id = _body.get('gameId')

    _game = JoinGame.execute(
            player_name=_player_name,
            game_id=_game_id)

    _token = AuthToken.create(
            game_id = _game.get('game_id'),
            player_id = _game.get('player_id'),
            player_name = _game.get('player_name'),
            ttl = _game.get('ttl'))

    return {
            'statusCode': 200,
            'body': json.dumps({
                'token': _token,
                'expires': _game.get('ttl')})}


