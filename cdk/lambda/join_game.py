
from common.join_game import JoinGame
from common.auth_token import AuthToken

def handler(event, context):

    # get player name from event
    # get number of decks from event

    _player_name = event.get('playerName')
    _game_id = event.get('gameId')

    _game = JoinGame.execute(
            player_name=_player_name,
            game_id=_game_id)

    return AuthToken.create(
            game_id = _game.get('game_id'),
            player_id = _game.get('player_id'),
            player_name = _game.get('player_name'),
            ttl = _game.get('ttl'))
