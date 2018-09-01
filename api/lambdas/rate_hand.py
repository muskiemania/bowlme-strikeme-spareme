import traceback
import bowl_game

def lambda_handler(event, context):

    game_id = 0
    player_id = 1

    try:
        bowl_game.RateHand.rate(game_id, player_id)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    return None
