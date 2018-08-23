import traceback
from lambdas import game

def lambda_handler(event, context):

    game_id = 0
    player_id = 1

    try:
        game.RateHand.rate(game_id, player_id)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    return None
