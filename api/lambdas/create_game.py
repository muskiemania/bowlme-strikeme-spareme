from bowl_game.create_game import CreateGame

def handler(event, context):
    # fetch input
    host_player_name = event.get('hostPlayerName', 'Anonymous')
    number_of_decks = event.get('numberOfDecks', '1')
    try:
        number_of_decks = int(number_of_decks)
    except:
        number_of_decks = 1
        
    # create game
    game_id = CreateGame.create(number_of_decks)
    
    # return game info to next step
    return {
        'statusCode': 200,
        'body': {
            'game_id': game_id,
            'host_player_name': host_player_name
        }
    }

'''
def post_handler(event, context):

    #fetch input...
    host_player_name = 'hostPlayerName' in event.keys() and event['hostPlayerName'] or 'Anonymous'
    number_of_decks = 'numberOfDecks' in event.keys() and event['numberOfDecks'] or 1

    #create game
    game_dto = bowl_game.CreateGame.create(host_player_name, number_of_decks)

    #create player
    created_player = bowl_game.CreatePlayer.create(host_player_name, game_dto.game_id)

    #create deck
    bowl_game.CreateDeck.create(game_dto.game_id, number_of_decks)

    #create response
    model = viewmodels.JoinGameModel(game_dto.game_id, created_player['playerId'], game_dto.game_key)

    #create jwt
    if not model.is_game_id_zero():

        jwt = Helpers().get_jwt(model.get_jwt_data())
        model.set_jwt(jwt)

    return model.json()

def get_handler(event, context):

    to_return = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {}
    }

    jwt = 'headers' in event.keys() and 'x-bowl-token' in event['headers'] and event['headers']['x-bowl-token'] or None

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
'''
