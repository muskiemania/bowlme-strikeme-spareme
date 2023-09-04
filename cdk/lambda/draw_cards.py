
from common.draw_cards import DrawCards

def handler(event, context):

    # get game id from event
    # get player name from event
    # get number of cards from event

    _game_id = event.get('gameId')
    _player_id = event.get('playerId')
    _cards = event.get('cards')

    if not isinstance(_cards, int):
        return 'need an int'

    if not _cards in [1,2,3,4,5,6]:
        return 'draw 1-6 cards'

    DrawCards.draw(
            game_id=_game_id,
            player_id=_player_id,
            cards=_cards)

    return 'OK'
