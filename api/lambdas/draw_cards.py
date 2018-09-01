import traceback
from lambdas import bowl_game

def lambda_handler(event, context):

    number_of_cards = 0 or 1

    game_id = 0
    player_id = 1
    key = ''

    #verify_game = game.Verify.verify_game_by_id
    #verify_player = game.Verify.verify_player_in_game
    #game_verified = verify_game(game_id, [GameStatus.STARTED])
    #player_verified = verify_player(game_id, player_id, [PlayerStatus.DEALT])

    #if game_verified and player_verified:
    try:
        game.DrawCards.draw(game_id, player_id, number_of_cards)
    except Exception as e:
        print 'whats the matter?'
        print e
        print traceback.format_exc()

    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id)
    my_game.setGameKey(key)

    return my_game.json()
