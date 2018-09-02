import bowl_game
#from .helpers import Helpers
#import viewmodels

def handler(event, context):

    #fetch input...
    player_name = event['playerName']
    game_key = event['key']
    game_id = event['gameId']

    #create player
    created_player = bowl_game.CreatePlayer.create(player_name, game_key)

    #create jwt
    #if not created_game.is_game_id_zero():

    #    jwt = Helpers().get_jwt(created_game.get_jwt_data())
    #    created_game.set_jwt(jwt)

    created_player['gameId'] = game_id
    return created_player
