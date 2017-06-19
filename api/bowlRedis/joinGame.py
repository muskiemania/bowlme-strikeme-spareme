import redis
import cards

class JoinGame:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.game_id = None
        self.player = None

    def init(self, joinGame):
        self.game_id = joinGame.game_id
        self.player = joinGame.player

    def execute(self):

        #need a list for the deck - game-id-deck
        #need a list for the discard - game-id-discard
        #need a list for each players hand game-id-player-hand
        #need a hash for game info: host, status game-id-info:
        #hash for each players name - game-id-name:playerid
        #hash for each players hand - game-id-status:playerid
        p = self.r.pipeline()
        p.hmset('game-%s-name' % self.game_id, {'%s' % self.player.player_id: self.player.player_name})
        p.hmset('game-%s-status' % self.game_id, {'%s' % self.player.player_id: 0})
        p.execute()

        return True

    def get(self, key, field=None):
        suffix = key.split('-')[2]
        if suffix == 'deck':
            return self.r.lrange(key, 0, -1)
        elif suffix == 'info' or suffix == 'name' or suffix == 'status':
            return self.r.hget(key, field)
