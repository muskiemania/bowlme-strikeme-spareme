from createPlayer import CreatePlayer
import bowlRedis

class JoinGame:

    def __init__(self, game_id = 0, player = None):
        self.game_id = game_id
        self.player = player

    def join(self, player_name = None):
        player = CreatePlayer(player_name, self.game_id)        

        return JoinGame(game_id=self.game_id,player=player)

    def execute(self):
        r = bowlRedis.join_game()
        r.init(self)
        
        if r.execute():
            return self.player.player_id
