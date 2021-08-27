import traceback
import bowl_game

def handler(event, context):

    # must fetch metadata
    game_id = ''
    player_id = ''

    dynamos.ScoreHand.score(game_id, player_id)
    
    return {
        'statusCode': 200,
        'body': 'OK'
    }
    
    '''
    try:
        bowl_game.RateHand.rate(game_id, player_id)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    return None
    '''
