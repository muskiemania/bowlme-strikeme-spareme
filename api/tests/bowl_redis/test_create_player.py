from entities import Player, PlayerStatus
import bowl_redis
import redis

class Test_RedisCreatePlayer:

    def test_create_player_constructor(self):
        game_id = 100
        player = Player('Justin', game_id)
        create_player = bowl_redis.CreatePlayer(player)
        
        assert create_player.player == player
        assert create_player.player.player_status == PlayerStatus.JOINED
        
    def test_create_player_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        game_id = 100
        player = Player('Justin', game_id)
        create_player = bowl_redis.CreatePlayer(player)
        player = create_player.execute(game_id)

        key_info = bowl_redis.RedisKeys(game_id, player.player_id)
        
        pipe.exists(key_info.game_players())
        pipe.lrange(key_info.game_players(), 0, -1)

        [player_exists, players] = pipe.execute()

        assert player_exists
        assert len(players) == 1
        assert player.player_id in players

        players_info_exists = pipe.exists(key_info.game_players_info())
        players_info_name_exists = pipe.hexists(key_info.game_players_info(), key_info.game_players_name_key())
        players_info_status_exists = pipe.hexists(key_info.game_players_info(), key_info.game_players_status_key())

        [players_info_exists, player_info_name_exists, player_info_status_exists] = pipe.execute()

        assert players_info_exists
        assert player_info_name_exists
        assert player_info_status_exists

        players_info_name = pipe.hget(key_info.game_players_info(), key_info.game_players_name_key())
        players_info_status = pipe.hget(key_info.game_players_info(), key_info.game_players_status_key())

        [player_info_name, player_info_status] = pipe.execute()

        assert player_info_name == 'Justin'
        assert player_info_status == str(PlayerStatus.JOINED.value)
