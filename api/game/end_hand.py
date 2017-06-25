import bowl_redis

class EndHand(object):

    def __init__(self, game_id=0, player_id=None):
        self.game_id = game_id
        self.player_id = player_id

    def end(self, player_id=None):
        return EndHand(game_id=self.game_id, player_id=player_id)

    def execute(self):
        redis = bowl_redis.end_hand()
        redis.init(self)

        if redis.execute():
            return self.player_id
