import bowl_redis
import cards
import scoring
import viewmodels

class Results(object):

    def __init__(self):
        pass

    @staticmethod
    def get(game_id):
        
        players = bowl_redis.GetPlayers(game_id)
        player_dto = players.execute()

        game_details = bowl_redis.GetGame(game_id)
        game_details_dto = game_details.execute()

        #needs:
        #all players - no separation of me vs them, including name, hand (if finished), and ranked
        #for the game
        #  -- need game status
        #  -- need to know if "I" am the host

        results = viewmodels.ResultsModel()

        results.setPlayers(player_dto)
        results.setStatus(game_details_dto.game_status)
        results.setHostPlayerId(game_details_dto.host_player_id)
            
        return results
