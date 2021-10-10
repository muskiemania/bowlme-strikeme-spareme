import traceback
import json
from bowl_game.discard_cards import DiscardCards

def handler(event, context):

    # must get data from event
   
    _body = event.get('body', '{}')
    _body = json.loads(_body)
    _game_id = _body.get('gameId')
    _player_id = _body.get('playerId')
    _cards = _body.get('cards')

    # must execute
    try:
        DiscardCards.discard(_game_id, _player_id, _cards)
    except:
        raise
    else:
        return {
            'statusCode': 200,
            'body': 'OK'
        }

    '''
    
    number_of_cards = 0 or 1

    game_id = 0
    player_id = 1
    key = ''

    #1: draw cards
    #2: should shuffle? yes: goto 3; no: goto 4
    #3: shuffle cards
    #4: should change player status? yes: goto 5; no: goto 6
    #5: change player status
    #6: should score and rank? yes: goto 7; no: goto 12
    #7: score hand
    #8: rank players
    #9: should change game status? yes: goto 10; no: goto 11
    #10: change game status
    #11: fetch game data and return

    bowl_game.DrawCards.draw(game_id, player_id, number_of_cards) #1

    if bowl_game.ShuffleCards.check(game_id): #2
        bowl_game.ShuffleCards.shuffle(game_id) #3

    if number_of_cards > 2: #4
        bowl_game.PlayerStatus.change(game_id, player_id, PlayerStatus.FINISHED) #5

    if bowl_game.Scoring.check(game_id, player_id): #6
        bowl_game.Scoring.score(game_id, player_id) #7
        bowl_game.Ranking.rank(game_id) #8

        if bowl_game.GameStatus.check(game_id): #9
            bowl_game.GameStatus.change(game_id, GameStatus.FINISHED) #10

    my_game = bowl_game.Game.get(game_id=game_id, player_id=player_id) #11
    my_game.setGameKey(key)

    return my_game.json()
    '''
