from bowl_redis_dto import PlayerDto, PlayerStatus
import bowl_redis
import redis

class Test_RedisCreatePlayer:

    def test_create_player_constructor(self):
        game_id = 100
        player = PlayerDto('Justin', game_id)
        create_player = bowl_redis.CreatePlayer(player)
        
        assert create_player.player == player
        assert create_player.player.player_status == PlayerStatus.JOINED
        
    def test_create_player_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        game_id = 100
        player = PlayerDto('Justin', game_id)
        create_player = bowl_redis.CreatePlayer(player)
        player = create_player.execute(game_id)

        key_info = bowl_redis.RedisKeys(game_id, player.player_id)

        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, player.player_id)

        assert helpers.verify_player_info_exists(game_id, player.player_id)
        assert helpers.verify_player_name_in_player_info(game_id, player.player_id)
        assert helpers.verify_player_name_eq_in_player_info(game_id, player.player_id, player.player_name)
        assert helpers.verify_player_status_in_player_info(game_id, player.player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, player.player_id, player.player_status)
