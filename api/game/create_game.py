import bowl_redis
import entities

class CreateGame(object):

    def __init__(self):
        pass

    @staticmethod
    def create(host_player_name):
        create_game = bowl_redis.CreateGame(host_player_name)
        game = create_game.execute()

        response = entities.APIGameResponse()
        response.game_id = game.game_id

        game_status = entities.APIGameStatus()
        game_status.game_status_id = game.game_status.value
        game_status.game_status_text = entities.GameStatus.text(game.game_status)
        
        response.game_status = game_status
        
        response.last_updated = entities.APILastUpdated(game.last_updated)

        player = game.players[0]
        response_player = entities.APIPlayerBase(player.player_id, player.player_name)
        response.player = response_player

        return response
