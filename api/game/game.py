import bowl_redis
import entities
import cards
import scoring
import viewmodels

class Game(object):

    def __init__(self):
        pass

    @staticmethod
    def get(game_id, player_id=None):
        
        players = bowl_redis.GetPlayers(game_id)
        player_dto = players.execute()

        game_details = bowl_redis.GetGame(game_id)
        game_details_dto = game_details.execute()

        #needs:
        #all players, including name, hand, status
        #if player specified, then
        #  -- exclude "me" from players
        #  -- fetch my cards
        #  -- fetch my status
        #for the game
        #  -- need game status
        #  -- need to know if "I" am the host

        my_game = viewmodels.MyGameModel()

        if player_id is not None:
            my_game.setOthers(filter(lambda x: not x.player_id == player_id, player_dto))
            my_game.setPlayer(filter(lambda x: x.player_id == player_id, player_dto)[0])
            my_game.setStatus(game_details_dto.game_status)
            my_game.setHostPlayerId(game_details_dto.host_player_id)
            
        return my_game
