import bowl_game
#import viewmodels

def handler(event, context):

    #fetch input...
    host_player_name = event['playerName']
    number_of_decks = event['numberOfDecks'] or 1

    #create game
    created_game = bowl_game.CreateGame.create(host_player_name, number_of_decks)

    #create jwt
    if not created_game.is_game_id_zero():

        jwt = Helpers().get_jwt(created_game.get_jwt_data())
        created_game.set_jwt(jwt)

    return created_game.json()
