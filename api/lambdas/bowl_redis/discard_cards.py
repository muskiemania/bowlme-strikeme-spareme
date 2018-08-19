import redis
from cards import Card, Deck
from . import RedisKeys

class DiscardCards(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

        self.discard_key = RedisKeys(game_id).game_discard()
        self.hand_key = RedisKeys(game_id, player_id).game_player_hand()

    def execute(self, cards):
        for card in cards:
            pipe = self.redis.pipeline()
            pipe.lrem(self.hand_key, 0, card)
            [success] = pipe.execute()

            if success == 1:
                pipe.rpush(self.discard_key, card)
                pipe.execute()

        pipe.lrange(self.hand_key, 0, -1)
        [hand] = pipe.execute()
        return hand or []
