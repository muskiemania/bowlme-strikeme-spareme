from entities import GameStatus, PlayerStatus
import bowlRedis
import redis

class Test_RedisCreateGame:

    def test_create_game_constructor(self):
        host_player_name = 'Justin'
        create_game = bowlRedis.CreateGame(host_player_name)
        assert create_game.host_player_name == host_player_name
        
    def test_create_game_get_new_game_id(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowlRedis.CreateGame('Justin')

        assert create_game._CreateGame__get_new_game_id() == 1
        assert create_game._CreateGame__get_new_game_id() == 2
                
    def test_create_game_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowlRedis.CreateGame('Justin')
        game = create_game.execute()

        game_info_exists = pipe.exists('game-%s-info' % game.game_id).execute()[0]
        game_info = pipe.hgetall('game-%s-info' % game.game_id).execute()[0]
        
        assert game_info_exists
        assert game_info['host_name'] == 'Justin'
        assert 'host_id' in game_info.keys()
        #assert game_info['status'] == GameStatus.CREATED

        game_last_updated_exists = pipe.exists('game-last-updated').execute()[0]
        game_last_updated_info = pipe.hgetall('game-last-updated').execute()[0]

        assert game_last_updated_exists
        assert game_last_updated_info['g%s-updated' % game.game_id] == str(game.last_updated)
        #assert game_last_updated_info['g%s-status' % game.game_id] == game.game_status

        player_exists = pipe.exists('game-%s-players' % game.game_id).execute()[0]
        player_name = pipe.hgetall('game-%s-players' % game.game_id).execute()[0]
        player_status_exists = pipe.exists('game-%s-player-statuses' % game.game_id).execute()[0]
        player_statuses = pipe.hgetall('game-%s-player-statuses' % game.game_id).execute()[0]

        assert player_exists
        host_id = game_info['host_id']
        assert host_id in player_name.keys()
        assert player_name[host_id] == 'Justin'

        assert player_status_exists
        assert host_id in player_statuses.keys()
        #assert player_statuses[host_id] == entities.PlayerStatus.JOINED
