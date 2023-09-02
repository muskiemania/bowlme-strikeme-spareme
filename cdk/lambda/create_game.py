
from common.create_game import CreateGame

def handler(event, context):

    # get player name from event
    # get number of decks from event

    _player_name = event.get('playerName')
    _decks = event.get('decks')

    return CreateGame.execute(
            player_name=_player_name,
            decks=_decks)
