from entities import GameStatus, PlayerStatus
import bowl_redis
import redis
from cards import Deck
import pytest

class Test_RedisStartGame:

    def test_start_game_constructor(self):
        game_id = 200
        start_game = bowl_redis.StartGame(game_id)
        assert start_game.game_id == game_id

    def test_start_game_execute_no_host_id(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        start_game = bowl_redis.StartGame(200)
        
        with pytest.raises(Exception) as exception:
            game = start_game.execute('asdfqwerty')
    
        assert exception.value.message == 'no host id available for this game'

    def test_start_game_execute_no_host_name(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        key_info = bowl_redis.RedisKeys(game.game_id)
        pipe.hdel(key_info.game_info(), key_info.game_info_host_name_key())
        pipe.execute()
        
        start_game = bowl_redis.StartGame(game.game_id)

        with pytest.raises(Exception) as exception:
            game = start_game.execute(game.players[0].player_id)
    
        assert exception.value.message == 'no host name available for this game'

    def test_start_game_execute_no_status(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        key_info = bowl_redis.RedisKeys(game.game_id)
        pipe.hdel(key_info.game_info(), key_info.game_info_status_key())
        pipe.execute()
        
        start_game = bowl_redis.StartGame(game.game_id)

        with pytest.raises(Exception) as exception:
            game = start_game.execute(game.players[0].player_id)
    
        assert exception.value.message == 'status unknown for this game'

    def test_start_game_execute_not_host(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        
        start_game = bowl_redis.StartGame(game.game_id)

        with pytest.raises(Exception) as exception:
            game = start_game.execute('Sarah')

        assert exception.value.message == 'only the host can start a game'

    def test_start_game_execute_wrong_status(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        start_game = bowl_redis.StartGame(game.game_id)
        start_game.execute(game.players[0].player_id)

        with pytest.raises(Exception) as exception:
            start_game.execute(game.players[0].player_id)

        assert exception.value.message == 'cannot start a game that is not in CREATED status'

    def test_start_game_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        players = game.players

        start_game = bowl_redis.StartGame(game.game_id)
        game = start_game.execute(game.players[0].player_id)
        
        # 1 - verify game status
        # 2 - verify deck
        # 3 - verify game last updated
        # 4 - verify player status

        helpers = bowl_redis.Helpers(pipe)
        #1
        assert helpers.verify_game_info_exists(game.game_id)
        #2
        assert helpers.verify_game_deck_exists(game.game_id)
        assert helpers.verify_game_deck_is_valid(game.game_id)
        #3
        assert helpers.verify_game_last_updated_exists()
        assert helpers.verify_game_updated_exists(game.game_id)
        assert helpers.verify_game_status_exists(game.game_id)
        assert helpers.verify_game_updated_eq_in_game_last_updated(game.game_id, game.last_updated)
        assert helpers.verify_game_status_eq_in_game_last_updated(game.game_id, game.game_status)
        #4
        assert helpers.verify_player_info_exists(game.game_id, players[0].player_id)
        assert helpers.verify_player_name_in_player_info(game.game_id, players[0].player_id)
        assert helpers.verify_player_status_in_player_info(game.game_id, players[0].player_id)
        assert helpers.verify_player_name_eq_in_player_info(game.game_id, players[0].player_id, players[0].player_name)
        assert helpers.verify_player_status_eq_in_player_info(game.game_id, players[0].player_id, players[0].player_status)
