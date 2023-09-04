
from common.game_status import GameStatus

def handler(event, context):

    # get player name from event
    # get number of decks from event

    _game_id = event.get('gameId')
    _status = event.get('status')

    if _status == 'start':
        _game = GameStatus.start(
                game_id=_game_id)
        return 'OK'

