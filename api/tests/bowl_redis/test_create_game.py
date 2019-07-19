import pytest
from bowl_redis_dto import GameDto, GameStatus, PlayerDto, PlayerStatus
import bowl_redis
import redis

@pytest.mark.skip(reason='hardening')
class Test_RedisCreateGame:

    def test_create_game_constructor(self):
        host_player_name = 'Justin'
        create_game = bowl_redis.CreateGame(host_player_name)
        assert create_game.host_player_name == host_player_name

    def test_create_game_get_new_game_id(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')

        assert create_game._CreateGame__get_new_game_id() == 1
        assert create_game._CreateGame__get_new_game_id() == 2

    def _setup_test_create_game(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        return (pipe, game)

    def test_create_game_execute_1(self):

        (pipe, game) = self._setup_test_create_game()

        #verify game-[game_id]-info exists and is populated
        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_info_exists(game.game_id)
        assert helpers.verify_host_id_exists_in_game_info(game.game_id)
        assert helpers.verify_host_name_exists_in_game_info(game.game_id)
        assert helpers.verify_status_exists_in_game_info(game.game_id)

        assert helpers.verify_host_id_eq_in_game_info(game.game_id, game.players[0].player_id)
        assert helpers.verify_host_name_eq_in_game_info(game.game_id, game.players[0].player_name)
        assert helpers.verify_status_eq_in_game_info(game.game_id, game.game_status)

    def test_create_game_execute_2(self):

        (pipe, game) = self._setup_test_create_game()

        #verify game_last_updated exists and is populated
        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_last_updated_exists()
        assert helpers.verify_game_updated_exists(game.game_id)
        assert helpers.verify_game_status_exists(game.game_id)

        assert helpers.verify_game_updated_eq_in_game_last_updated(game.game_id, game.last_updated)
        assert helpers.verify_game_status_eq_in_game_last_updated(game.game_id, game.game_status)

    def test_create_game_execute_3(self):

        (pipe, game) = self._setup_test_create_game()

        #verify game-[game_id]-players exists and is populated
        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_players_exists(game.game_id)
        assert helpers.verify_player_id_in_game_players(game.game_id, game.players[0].player_id)

    def test_create_game_execute_4(self):

        (pipe, game) = self._setup_test_create_game()

        #verify game-[game_id]-players-info exists and is populated
        helpers = bowl_redis.Helpers(pipe)
        player_id = game.players[0].player_id

        print(game.game_id)
        print(player_id)

        assert helpers.verify_player_info_exists(game.game_id, player_id)
        assert helpers.verify_player_name_in_player_info(game.game_id, player_id)
        assert helpers.verify_player_status_in_player_info(game.game_id, player_id)

        player_name = game.players[0].player_name
        player_status = game.players[0].player_status
        assert helpers.verify_player_name_eq_in_player_info(game.game_id, player_id, player_name)
        assert helpers.verify_player_status_eq_in_player_info(game.game_id, player_id, player_status)
