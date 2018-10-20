import bowl_game

def handler(event, context):

    #return {'hello': 'world'}

    #return context.keys()

    game_id = 'gameId' in event.keys() and event['gameId'] or None
    player_id = 'playerId' in event.keys() and event['playerId'] or None
    game_key = 'key' in event.keys() and event['key'] or None

    return {
        'hello': 'world',
        'gameId': game_id or 9999,
        'playerId': player_id or 8888,
        'key': game_key or 'KKEEYY'
    }

    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id)
    my_game.set_game_key(game_key)

    return my_game.json()
