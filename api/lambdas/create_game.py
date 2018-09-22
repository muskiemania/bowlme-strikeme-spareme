import bowl_game
from helpers import Helpers
import viewmodels

def post_handler(event, context):

    #fetch input...
    host_player_name = event['hostPlayerName']
    number_of_decks = event['numberOfDecks'] or 1

    #create game
    created_game = bowl_game.CreateGame.create(host_player_name, number_of_decks)

    #create jwt
    if not created_game.is_game_id_zero():

        jwt = Helpers().get_jwt(created_game.get_jwt_data())
        created_game.set_jwt(jwt)

    to_return = created_game.json()
    to_return['playerName'] = host_player_name
    to_return['numberOfDecks'] = number_of_decks

    return to_return

def get_handler(event, context):

    game_is_verified = context['gameIsVerified']
    player_is_verified = context['playerIsVerified']

    if not game_is_verified or not player_is_verified:
        null_game = viewmodels.JoinGameModel(0, 0, None)
        return null_game.json()

    game_id = context['gameId']
    player_id = context['playerId']
    key = context['key']

    created_game = viewmodels.JoinGameModel(game_id, player_id, key)
    return created_game.json()
