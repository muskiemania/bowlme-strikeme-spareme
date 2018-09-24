import bowl_game
from helpers import Helpers

def handler(event, context):

    game_key = 'key' in event.keys() and event['key'] or None
    player_name = 'playerName' in event.keys() and event['playerName'] or None

    #join game
    join_game = bowl_game.JoinGame(game_key)
    joined_game = join_game.execute(player_name)

    #create cookie
    if not joined_game.is_game_id_zero():
        jwt = Helpers().get_jwt(joined_game.get_jwt_data())
        joined_game.set_jwt(jwt)

    return joined_game.json()
