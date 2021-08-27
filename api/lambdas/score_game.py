import traceback
import bowl_game

def handler(event, context):

    # fetch metadata
    game_id = ''
    
    dynamos.ScoreGame.score(game_id)
    
    return {
        'statusCode': 200,
        'body': 'OK'
    }

    '''
    try:
        bowl_game.RankHands.rank(game_id)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    return None
    '''
