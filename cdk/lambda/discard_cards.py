
from common.discard_cards import DiscardCards

def handler(event, context):

    # get game id from event
    # get player name from event
    # get number of cards from event

    _game_id = event.get('gameId')
    _player_id = event.get('playerId')
    _cards = event.get('cards')

    if not isinstance(_cards, list):
        return 'need a list'

    if not len(_cards) in [1,2,3,4,5,6]:
        return 'discard 1-6 cards'

    DiscardCards.discard(
            game_id=_game_id,
            player_id=_player_id,
            cards=_cards)

    return 'OK'
