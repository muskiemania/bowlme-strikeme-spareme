import bowl_redis
from bowl_redis_dto import PlayerDto

class JoinGame(object):

    def __init__(self):
        pass

    @staticmethod
    def join(game_id, player_name=None):
        playerDto = PlayerDto(player_name, game_id)

        create_player = bowl_redis.CreatePlayer(playerDto)
        playerDto = create_player.execute(game_id)

        #response = entities.APIGameResponse()
        #response.game_id = game_id

        gameDto = bowl_redis.GetGame(game_id)
        print gameDto.__dict__
        #game = get_game.get()

        #game_status = entities.APIGameStatus()
        #game_status.game_status_id = game.game_status.value
        #game_status.game_status_text = entities.GameStatus.text(game.game_status)
        #response.game_status = game_status

        #response.last_updated = entities.APILastUpdated(game.last_updated)

        #response_player = entities.APIPlayerBase(player.player_id, player.player_name)
        #response.player = response_player

        return gameDto
