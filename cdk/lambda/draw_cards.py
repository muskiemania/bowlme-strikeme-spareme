import json
from common.draw_cards import DrawCards
from common.helper import Helper


def handler(event, context):

    try:
        _auth_context = event.get('requestContext', {}).get('authorizer', {}).get('lambda', {})
        
        _game_id = _auth_context['gameId']
        _player_id = _auth_context['playerId']
        _player_name = _auth_context['playerName']
    except:
        traceback.print_exc()

    # get number of cards from event
    _body = json.loads(event.get('body'))
    _cards = _body.get('cards')

    print(_cards)

    if not isinstance(_cards, int):
        return 'need an int'

    if not _cards in [1,2,3,4,5,6]:
        return 'draw 1-6 cards'

    DrawCards.draw(
            game_id=_game_id,
            player_id=_player_id,
            cards=_cards)

    return {
            'statusCode': 200,
            'body': json.dumps({
                'hand': Helper.get_player_hand(
                    game_id=_game_id,
                    player_id=_player_id)})}
