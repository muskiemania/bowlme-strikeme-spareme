import traceback
import bowl_game

def lambda_handler(event, context):

    game_id = 0

    try:
        bowl_game.RankHands.rank(game_id)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    return None
