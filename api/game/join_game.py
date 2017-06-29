import bowl_redis
import entities

class JoinGame(object):

    def __init__(self):
        pass

    @staticmethod
    def join(game_id, player_name=None):
        player = entities.Player(player_name, game_id)
        create_player = bowl_redis.CreatePlayer(player)
        player = create_player.execute(game_id)

        response = entities.APIGameResponse()
        response.game_id = game_id

        get_game = bowl_redis.GetGame(game_id)
        game = get_game.get()

        game_status = entities.APIGameStatus()
        game_status.game_status_id = game.game_status.value
        game_status.game_status_text = entities.GameStatus.text(game.game_status)
        response.game_status = game_status

        response.last_updated = entities.APILastUpdated(game.last_updated)

        response_player = entities.APIPlayerBase(player.player_id, player.player_name)
        response.player = response_player

        return response
