from lambdas import game, viewmodels
from . import Helpers

def lambda_handler(event, context):

    game_key = ''
    player_name = ''

    #join game
    join_game = game.JoinGame(game_key)
    joined_game = join_game.execute(player_name)

    #create cookie
    if not joined_game.is_game_id_zero():
        jwt = Helpers().get_jwt(joined_game.get_jwt_data())
        joined_game.set_jwt(jwt)

    return joined_game.json()
