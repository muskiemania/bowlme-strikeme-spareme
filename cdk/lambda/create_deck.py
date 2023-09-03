from common.create_deck import CreateDeck

def handler(event, context):

    _detail = event.get('detail')
    
    _action = _detail.get('Action')
    _game_id = _detail.get('Game_Id')
    _decks = _detail.get('Decks')

    if _action != 'create_deck':
        return

    if not isinstance(_decks, int):
        _decks = 1

    if _decks > 10:
        _decks = 10

    CreateDeck.create(_game_id, _decks)

    return

