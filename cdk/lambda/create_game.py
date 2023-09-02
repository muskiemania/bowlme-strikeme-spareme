
from common.create_game import CreateGame
from common.auth_token import AuthToken

def handler(event, context):

    # get player name from event
    # get number of decks from event

    _player_name = event.get('playerName')
    _decks = event.get('decks')

    _game = CreateGame.execute(
            player_name=_player_name,
            decks=_decks)

    return AuthToken.create(
            game_id = _game.get('game_id'),
            player_id = _game.get('player_id'),
            player_name = _game.get('player_name'),
            ttl = _game.get('ttl'))
