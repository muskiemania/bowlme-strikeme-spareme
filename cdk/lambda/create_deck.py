from common.create_deck import CreateDeck

def handler(event, context):

    _game_id = event.get('gameId')
    _decks = event.get('decks')

    if not isinstance(_decks, int)):
        _decks = 1

    if _decks > 10:
        _decks = 10

    CreateDeck.create(_game_id, _decks)

    return

