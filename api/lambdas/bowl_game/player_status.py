import bowl_redis

class PlayerStatus(object):

    def __init__(self):
        pass

    @staticmethod
    def set(game_id, player_status):
        status = bowl_redis.SetPlayerStatus(game_id)
        status.set(player_status)
        return
