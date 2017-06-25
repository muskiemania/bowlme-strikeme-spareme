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

        key_info = bowl_redis.RedisKeys(game.game_id)
        
        game_info_exists = pipe.exists(key_info.game_info()).execute()[0]
        game_info = pipe.hgetall(key_info.game_info()).execute()[0]
        
        assert game_info_exists
        assert game_info['host_name'] == 'Justin'
        assert 'host_id' in game_info.keys()
        assert game_info['status'] == str(GameStatus.CREATED.value)

        game_last_updated_exists = pipe.exists(key_info.game_last_updated()).execute()[0]
        game_last_updated_info = pipe.hgetall(key_info.game_last_updated()).execute()[0]

        assert game_last_updated_exists
        assert game_last_updated_info[key_info.game_last_updated_key()] == str(game.last_updated)
        assert game_last_updated_info[key_info.game_last_updated_status_key()] == str(game.game_status.value)

        player_exists = pipe.exists(key_info.game_players()).execute()[0]
        player_name = pipe.hgetall(key_info.game_players()).execute()[0]
        player_status_exists = pipe.exists(key_info.game_player_statuses()).execute()[0]
        player_statuses = pipe.hgetall(key_info.game_player_statuses()).execute()[0]

        assert player_exists
        host_id = game_info['host_id']
        assert host_id in player_name.keys()
        assert player_name[host_id] == 'Justin'

        assert player_status_exists
        assert host_id in player_statuses.keys()
        assert player_statuses[host_id] == str(PlayerStatus.JOINED.value)
