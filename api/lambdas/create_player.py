import bowl_game
#from .helpers import Helpers
#import viewmodels

def handler(event, context):

    #fetch input...
    player_name = event.get('playerName', 'Anonymous')
    game_hash = event.get('gameId')
    
    if game_hash is None:
        raise Exception('gameId is required')
    
    player_id = dynamos.CreatePlayer.create(player_name, game_hash, False)
    
    return {
        'statusCode': 200,
        'body': {
            'gameId': game_hash,
            'playerId': player_id
        }
    }
