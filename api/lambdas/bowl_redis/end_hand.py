import redis
import bowl_redis
from bowl_redis_dto import GameStatus, PlayerStatus
from scoring import Scorer

class EndHand(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

    def execute(self):
        pipe = self.redis.pipeline()

        key_info = bowl_redis.RedisKeys(self.game_id, self.player_id)

        #first verify that game is started and player status is dealt
        helpers = bowl_redis.Helpers(pipe)

        verify_game = helpers.verify_status_eq_in_game_info

        game_status_started = verify_game(self.game_id, GameStatus.STARTED)
        game_status_created = verify_game(self.game_id, GameStatus.CREATED)
        game_status_others = not game_status_started and not game_status_created

        if game_status_others:
            raise Exception('cannot end a hand for a game that is not started or created')

        player_in_game = helpers.verify_player_id_in_game_players(self.game_id, self.player_id)

        if not player_in_game:
            raise Exception('cannot end a hand for a player that is not playing this game')

        verify_player = helpers.verify_player_status_eq_in_player_info

        player_status_joined = verify_player(self.game_id, self.player_id, PlayerStatus.JOINED)
        player_status_dealt = verify_player(self.game_id, self.player_id, PlayerStatus.DEALT)
        player_status_others = not player_status_joined and not player_status_dealt

        if player_status_others:
            raise Exception('cannot end a hand for a player that is not joined or dealt')

        players_info_key = key_info.game_players_info()
        players_status_key = key_info.game_players_status_key()

        if game_status_created:
            pipe.hset(players_info_key, players_status_key, PlayerStatus.ABANDONED)
        if game_status_started:
            pipe.hset(players_info_key, players_status_key, PlayerStatus.FINISHED)

        pipe.execute()

        return
