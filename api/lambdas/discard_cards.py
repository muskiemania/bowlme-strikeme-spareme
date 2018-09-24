import traceback
import bowl_game

def lambda_handler(event, context):

    game_id = 1
    player_id = 2
    discard_cards = 1

    #1: draw cards
    #2: should change player status? yes: goto 3; no: goto 4
    #3: change player status
    #4: should score and rank? yes: goto 5; no: goto 9
    #5: score hand
    #6: rank players
    #7: should change game status? yes: goto 8; no: goto 9
    #8: change game status
    #9: fetch game data and return

    bowl_game.DiscardCards.discard(game_id, player_id, number_of_cards) #1

    if number_of_cards > 2: #2
        bowl_game.PlayerStatus.change(game_id, player_id, PlayerStatus.FINISHED) #3

    if bowl_game.Scoring.check(game_id, player_id): #4
        bowl_game.Scoring.score(game_id, player_id) #5
        bowl_game.Ranking.rank(game_id) #6

        if bowl_game.GameStatus.check(game_id): #7
            bowl_game.GameStatus.change(game_id, GameStatus.FINISHED) #8

    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id) #9
    my_game.setGameKey(key)

    return my_game.json()
