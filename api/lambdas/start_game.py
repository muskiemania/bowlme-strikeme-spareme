import traceback
import bowl_game
from bowl_redis_dto import GameStatus, PlayerStatus

def handler(event, context):

    game_id = 'gameId' in event.keys() and event['gameId'] or 0
    player_id = 'playerId' in event.keys() and event['playerId'] or 1
    key = 'key' in event.keys() and event['key'] or 'key'

    #shuffle
    bowl_game.ShuffleDeck.shuffle(game_id)

    #change game status
    bowl_game.GameStatus.set(game_id, GameStatus.STARTED)

    #change player statuses
    bowl_game.PlayerStatus.set(game_id, PlayerStatus.DEALT)
    
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
