import bowl_game
from helpers import Helpers
from bowl_redis_dto import GameStatus
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

    to_return = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {}
    }

    jwt = 'headers' in event.keys() and 'X-Bowl-Token' in event['headers'] and event['headers']['X-Bowl-Token'] or None

    if jwt is None:
        null_game = viewmodels.JoinGameModel(0, 0, None)
        to_return['body'] = null_game.json()
        return to_return

    decoded = Helpers().decode_jwt(jwt)

    game_id = 'gameId' in decoded.keys() and decoded['gameId'] or None
    player_id = 'playerId' in decoded.keys() and decoded['playerId'] or None
    key = 'key' in decoded.keys() and decoded['key'] or None

    game_statuses = [GameStatus.CREATED, GameStatus.STARTED]

    game_is_verified = bowl_game.Verify.verify_game_by_id(game_id, game_statuses)
    player_is_verified = bowl_game.Verify.verify_player_in_game(game_id, player_id)

    if not game_is_verified or not player_is_verified:
        null_game = viewmodels.JoinGameModel(0, 0, None)
        to_return['body'] = null_game.json()
        return to_return

    game_id = 'gameId' in context.keys() and context['gameId'] or 0
    player_id = 'playerId' in context.keys() and context['playerId'] or 0
    key = 'key' in context.keys() and context['key'] or None

    created_game = viewmodels.JoinGameModel(game_id, player_id, key)
    to_return['body'] = created_game.json()
    return to_return
