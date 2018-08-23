import traceback
from lambdas import game

def lambda_handler(event, context):

    game_id = 0

    try:
        game.RankHands.rank(game_id)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    return None
