import redis
from create_player import CreatePlayer
from entities import Game, GameStatus, Player, PlayerStatus

class CreateGame:
   
    def __init__(self, host_player_name):
        self.redis = redis.StrictRedis()
        self.host_player_name = host_player_name

    def execute(self):

        game_id = self.__get_new_game_id()
        game = Game(game_id, self.host_player_name)
        game.game_status = GameStatus.CREATED
        
        info = {}
        info['status'] = game.game_status
        info['host_name'] = self.host_player_name

        last_updated = {}
        last_updated['g%s-updated' % game_id] = game.last_updated
        last_updated['g%s-status' % game_id] = game.game_status

        pipe = self.redis.pipeline()
        pipe.hmset('game-%s-info' % game_id, info)
        pipe.hmset('game-last-updated', last_updated)
        pipe.execute()

        player = Player(self.host_player_name, game.game_id)

        info['host_id'] = player.player_id
        pipe.hmset('game-%s-info' % game_id, info)
        pipe.execute()

        CreatePlayer(player).execute(game.game_id)

        game.players.append(player)

        return game

    def __get_new_game_id(self):
        pipe = self.redis.pipeline()
        pipe.incr('game-id-counter', 1)
        game_id = pipe.execute()
        if len(game_id) == 1:
            return game_id[0]
        return None
