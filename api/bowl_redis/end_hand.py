import redis
from . import RedisKeys
from entities import GameStatus, PlayerStatus
from scoring import Scorer

class EndHand(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

    def execute(self):
        pipe = self.redis.pipeline()

        key_info = RedisKeys(self.game_id, self.player_id)

        #first verify that game is started and player status is dealt
        pipe.hget(key_info.game_info(), key_info.game_info_status_key())
        pipe.hget(key_info.game_players_info(), key_info.game_players_status_key())
        [game_status, player_status] = pipe.execute()

        print 'player-status: ' + PlayerStatus(player_status)
        
        if game_status not in [str(GameStatus.STARTED.value), str(GameStatus.CREATED.value)]:
            raise Exception('cannot end a hand for a game that has not started')
        if player_status not in [str(PlayerStatus.JOINED.value), str(PlayerStatus.DEALT.value)]:
            raise Exception('cannot end a hand for this player')
        
        #game created                 --> player abandoned
        #game started + player dealt  --> player finished

        if game_status == str(GameStatus.CREATED.value):
            pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), PlayerStatus.ABANDONED.value)
        if game_status == str(GameStatus.STARTED.value) and player_status == str(PlayerStatus.DEALT):
            pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), PlayerStatus.FINISHED.value)
            
        pipe.execute()

        return
