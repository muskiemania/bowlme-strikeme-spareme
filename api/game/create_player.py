import bowl_redis
import entities

class CreatePlayer(object):

    def __init__(self):
        pass

    @staticmethod
    def create(self, player_name, game_id):
        player = entities.Player(player_name, game_id)
        create_player = bowl_redis.CreatePlayer(player)
        return create_player.execute(game_id)
