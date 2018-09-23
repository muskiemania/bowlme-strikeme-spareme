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

    #print 'xxxxx1'
    #print context
    #print 'yyyyy1'

    #authorizer = context['authorizer']
    #game_is_verified = 'gameIsVerified' in authorizer.keys() and authorizer['gameIsVerified'] or False
    #player_is_verified = 'playerIsVerified' in authorizer.keys() and authorizer['playerIsVerified'] or False

    #if not game_is_verified or not player_is_verified:
    #    null_game = viewmodels.JoinGameModel(0, 0, None)
    #    return null_game.json()

    #game_id = 'gameId' in authorizer.keys() and authorizer['gameId'] or 0
    #player_id = 'playerId' in authorizer.keys() and authorizer['playerId'] or 0
    #key = 'key' in authorizer.keys() and authorizer['key'] or None

    #created_game = viewmodels.JoinGameModel(game_id, player_id, key)
    #return created_game.json()

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {
            'hello': 'there',
            #'context': context
        }
    }
