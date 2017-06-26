from entities import GameStatus, PlayerStatus
import bowl_redis
import redis

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
                
    def test_create_game_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        key_info = bowl_redis.RedisKeys(game.game_id, game.players[0].player_id)

        #verify game-[game_id]-info exists and is populated
        pipe.exists(key_info.game_info())
        pipe.hgetall(key_info.game_info())
        [game_info_exists, game_info] = pipe.execute()
        
        assert game_info_exists
        assert game_info[key_info.game_info_host_name_key()] == 'Justin'
        assert key_info.game_info_host_id_key() in game_info.keys()
        assert game_info[key_info.game_info_status_key()] == str(GameStatus.CREATED.value)

        #verify game_last_updated exists and is populated
        pipe.exists(key_info.game_last_updated())
        pipe.hgetall(key_info.game_last_updated())
        [game_last_updated_exists, game_last_updated_info] = pipe.execute()
        
        assert game_last_updated_exists
        assert game_last_updated_info[key_info.game_last_updated_key()] == str(game.last_updated)
        assert game_last_updated_info[key_info.game_last_updated_status_key()] == str(game.game_status.value)

        #verify game-[game_id]-players exists and is populated
        pipe.exists(key_info.game_players())
        pipe.lrange(key_info.game_players(), 0, -1)
        [players_exists, players_list] = pipe.execute()

        assert players_exists
        assert len(players_list) == 1
        host_id = game_info[key_info.game_info_host_id_key()]
        assert players_list[0] == host_id

        #verify game-[game_id]-players-info exists and is populated
        pipe.exists(key_info.game_players_info())
        pipe.hgetall(key_info.game_players_info())
        [player_info_exists, player_info] = pipe.execute()
        
        assert player_info_exists
        assert player_info[key_info.game_players_name_key()] == 'Justin'
        assert player_info[key_info.game_players_status_key()] == str(PlayerStatus.JOINED.value)
