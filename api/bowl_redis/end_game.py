import redis
import bowl_redis
from entities import Game, GameStatus, PlayerStatus
from scoring import Scorer
import datetime

class EndGame(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self, player_id):
        pipe = self.redis.pipeline()

        key_info = bowl_redis.RedisKeys(self.game_id, player_id)

        #first verify that game is started and player status is dealt
        helpers = bowl_redis.Helpers(pipe)
        game_status_started = helpers.verify_status_eq_in_game_info(self.game_id, GameStatus.STARTED)
        game_status_created = helpers.verify_status_eq_in_game_info(self.game_id, GameStatus.CREATED)
        game_status_others = not game_status_started and not game_status_created

        if game_status_others:
            raise Exception('cannot end game that is not started or created')

        #then verify that the user is the host
        player_is_host = helpers.verify_host_id_eq_in_game_info(self.game_id, player_id)

        if not player_is_host:
            raise Exception('only the host of the game can end it')
        
        pipe.lrange(key_info.game_players(), 0, -1)
        pipe.hgetall(key_info.game_info())
        pipe.hgetall(key_info.game_players_info())

        [players, game_info, players_info] = pipe.execute()

        for player_id in players:
            key_info = bowl_redis.RedisKeys(self.game_id, player_id)
            player_is_joined = helpers.verify_player_status_eq_in_player_info(self.game_id, player_id, PlayerStatus.JOINED)
            player_is_dealt = helpers.verify_player_status_eq_in_player_info(self.game_id, player_id, PlayerStatus.DEALT)

            if player_is_joined:
                pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), PlayerStatus.ABANDONED)
            if player_is_dealt:
                pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), PlayerStatus.FINISHED)

        game = Game(self.game_id, game_info[key_info.game_info_host_name_key()])
        game.last_updated = datetime.datetime.now()

        if game_status_started:
            game.game_status = GameStatus.FINISHED
        if game_status_created:
            game.game_status = GameStatus.ABANDONED
            
        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), game.game_status)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), game.last_updated)

        pipe.execute()

        return game
