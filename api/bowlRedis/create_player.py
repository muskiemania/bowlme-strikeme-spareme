import redis
from entities import Player, PlayerStatus

class CreatePlayer(object):
   
    def __init__(self, player):
        self.redis = redis.StrictRedis()
        player.player_status = PlayerStatus.JOINED
        self.player = player
        

    def execute(self, game_id):
        players = {}
        players[self.player.player_id] = self.player.player_name

        statuses = {}
        statuses[self.player.player_id] = str(self.player.player_status.value)

        pipe = self.redis.pipeline()
        pipe.hmset('game-%s-players' % game_id, players)
        pipe.hmset('game-%s-player-statuses' % game_id, statuses)
        pipe.execute()
