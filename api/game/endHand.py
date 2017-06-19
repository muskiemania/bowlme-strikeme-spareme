import bowlRedis

class EndHand:

    def __init__(self, game_id = 0, player_id = None):
        self.game_id = game_id
        self.player_id = player_id

    def end(self, player_id = None):
        return EndHand(game_id=self.game_id,player_id=player_id)

    def execute(self):
        r = bowlRedis.end_hand()
        r.init(self)
        
        if r.execute():
            return self.player_id
