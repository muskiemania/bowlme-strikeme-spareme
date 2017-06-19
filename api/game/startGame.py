import bowlRedis

class StartGame:

    def __init__(self, game_id = 0, player_id = None):
        self.game_id = game_id
        self.player_id = player_id

    def start(self, player_id = None):
        return StartGame(game_id=self.game_id,player_id=player_id)

    def execute(self):
        r = bowlRedis.start_game()
        r.init(self)
        
        if r.execute():
            return self.game_id
