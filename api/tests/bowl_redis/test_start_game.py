from bowl_redis_dto import GameStatus, PlayerStatus
import bowl_redis
import redis
from cards import Deck
from scoring import Scorer
import pytest

class Test_RedisStartGame:

    def test_start_game_constructor(self):
        game_id = 200
        start_game = bowl_redis.StartGame(game_id)
        assert start_game.game_id == game_id

    def test_start_game_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        game_id = game.game_id
        player = game.players[0]
        player_name = player.player_name
        player_id = player.player_id

        start_game = bowl_redis.StartGame(game_id)
        start_game.default_rating = Scorer.default_rating()
        start_game.execute()
        
        # 1 - verify game status
        # 2 - verify deck
        # 3 - verify game last updated
        # 4 - verify player status
        # 5 - verify player has default rating and default rank

        helpers = bowl_redis.Helpers(pipe)
        #1
        assert helpers.verify_game_info_exists(game_id)
        #2
        assert helpers.verify_game_deck_exists(game_id)
        assert helpers.verify_game_deck_is_valid(game_id)
        #3
        assert helpers.verify_game_last_updated_exists()
        assert helpers.verify_game_updated_exists(game_id)
        assert helpers.verify_game_status_exists(game_id)
        #assert helpers.verify_game_updated_eq_in_game_last_updated(game_id, last_updated)
        assert helpers.verify_game_status_eq_in_game_last_updated(game_id, GameStatus.STARTED)
        #4
        assert helpers.verify_player_info_exists(game_id, player_id)
        assert helpers.verify_player_name_in_player_info(game_id, player_id)
        assert helpers.verify_player_status_in_player_info(game_id, player_id)
        assert helpers.verify_player_name_eq_in_player_info(game_id, player_id, player_name)
        assert helpers.verify_player_status_eq_in_player_info(game_id, player_id, PlayerStatus.DEALT)

        #5
        assert helpers.verify_player_rating_eq_in_player_info(game_id, player_id, Scorer.default_rating().as_string())
        assert helpers.verify_player_ranking_eq_in_player_info(game_id, player_id, 1)
