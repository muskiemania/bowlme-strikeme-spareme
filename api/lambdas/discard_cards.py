import traceback
import bowl_game

def lambda_handler(event, context):

    game_id = 1
    player_id = 2
    discard_cards = 1

    try:
        bowl_game.DiscardCards.discard(game_id, player_id, discard_cards)
    except Exception as e:
        print traceback.print_exc()

    return None
