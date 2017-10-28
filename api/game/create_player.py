import bowl_redis
from bowl_redis_dto import PlayerDto, RatingDto 
import scoring

class CreatePlayer(object):

    def __init__(self):
        pass

    @staticmethod
    def create(player_name, game_id):
        playerDto = PlayerDto(player_name, game_id)
        playerDto.player_rating = RatingDto(scoring.Scorer.default_rating())
        create_player = bowl_redis.CreatePlayer(playerDto)
        return create_player.execute(game_id)
