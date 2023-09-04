
from common.shuffle_deck import ShuffleDeck


def handler(event, context):

    _detail = event.get('detail')
    
    _action = _detail.get('Action')
    _game_id = _detail.get('Game_Id')

    if _action != 'shuffle_deck':
        return

    ShuffleDeck.shuffle(game_id=_game_id)

    return
