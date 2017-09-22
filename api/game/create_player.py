import bowl_redis
from bowl_redis_dto import PlayerDto 

class CreatePlayer(object):

    def __init__(self):
        pass

    @staticmethod
    def create(player_name, game_id):
        playerDto = PlayerDto(player_name, game_id)
        create_player = bowl_redis.CreatePlayer(playerDto)
        return create_player.execute(game_id)
