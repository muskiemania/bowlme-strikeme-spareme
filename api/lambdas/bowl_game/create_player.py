import bowl_redis
from bowl_redis_dto import PlayerDto, PlayerStatus, RatingDto
import scoring

class CreatePlayer(object):

    def __init__(self):
        pass

    @staticmethod
    def create(player_name, game_id):
        player_dto = PlayerDto(player_name, game_id)
        player_dto.player_status = PlayerStatus.JOINED
        player_dto.player_rating = RatingDto(scoring.Scorer.default_rating())
        create_player = bowl_redis.CreatePlayer(player_dto)
        return create_player.execute(game_id)
