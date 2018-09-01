import traceback
from lambdas import bowl_game

def lambda_handler(event, context):

    game_id = 0
    player_id = 1
    key = ''

    try:
        bowl_game.StartGame.start(game_id)
        print 'started ok'
    except Exception as e:
        print 'something went wrong'
        print e
        print e.args
        print traceback.format_exc()

    print 'hello there'
    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id)
    my_game.setGameKey(key)

    return my_game.json()
