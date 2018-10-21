import bowl_game

def handler(event, context):

    game_id = 'gameId' in event.keys() and event['gameId'] or None
    player_id = 'playerId' in event.keys() and event['playerId'] or None
    game_key = 'key' in event.keys() and event['key'] or None

    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id)
    my_game.set_game_key(game_key)

    return my_game.json()
