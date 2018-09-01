from lambdas import bowl_game
from lambdas.bowl_redis_dto import GameStatus

def lambda_handler(event, context):
    game_id = None #cherrypy.request.cookie['game_auth']
    player_id = None #cherrypy.request.cookie['player_auth']

    game_verified = bowl_game.Verify.verify_game_by_id(game_id, [GameStatus.CREATED])
    player_verified = bowl_game.Verify.verify_player_in_game(game_id, player_id)
    player_is_host = bowl_game.Verify.verify_player_is_host(game_id, player_id)

    return {
        'gameVerified': game_verified,
        'playerVerified': player_verified,
        'playerIsHost': player_is_host
    }
