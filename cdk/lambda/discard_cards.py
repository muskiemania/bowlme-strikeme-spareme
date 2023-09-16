import json
from common.discard_cards import DiscardCards
from common.helper import Helper

def handler(event, context):

    # get game id from auth
    # get player from auth
    try:
        _auth_context = event.get('requestContext', {}).get('authorizer', {}).get('lambda', {})
        
        _game_id = _auth_context['gameId']
        _player_id = _auth_context['playerId']
        _player_name = _auth_context['playerName']
    except:
        traceback.print_exc()


    # get cards from event
    _body = json.loads(event.get('body'))
    _cards = _body.get('cards')

    if not isinstance(_cards, list):
        return 'need a list'

    if not len(_cards) in [1,2,3,4,5,6]:
        return 'discard 1-6 cards'

    DiscardCards.discard(
            game_id=_game_id,
            player_id=_player_id,
            cards=_cards)

    return {
            'statusCode': 200,
            'body': json.dumps({
                'hand': Helper.get_player_hand(
                    game_id=_game_id,
                    player_id=_player_id)})}

