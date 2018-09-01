import bowl_game

def lambda_handler(event, context):

    game_id = 0
    player_id = 1
    key = ''

    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id)
    my_game.setGameKey(key)

    return my_game.json()
