
from common.helper import Helper
from core.card import Card
from core.hand import Hand
from core.scorer import Scorer

def handler(event, context):

    _detail = event.get('detail')
   
    _action = _detail.get('Action')
    _game_id = _detail.get('Game_Id')
    _player_id = _detail.get('Player_Id')

    if _action != 'score_hand':
        return

    _hand = Helper.get_player_hand(
            game_id=_game_id,
            player_id=_player_id)

    cards = [Card(c) for c in _hand]
    hand = Hand(cards)
    rating = Scorer(hand).get_rating()

    Helper.record_score(
            game_id=_game_id,
            player_id=_player_id,
            rating=rating)

    return
