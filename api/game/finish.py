import bowl_redis
from bowl_redis_dto import PlayerStatus

class Finish(object):

    def __init__(self):
        pass

    @staticmethod
    def execute(game_id, player_id):

        finish = bowl_redis.Players(game_id, player_id)
        finish.setPlayerStatus(PlayerStatus.FINISHED)

        return

    
    
