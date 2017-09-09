from entities import GameStatus, PlayerStatus
import bowl_redis
import redis
import pytest

class Test_RedisEndGame:

    def test_end_game_constructor(self):
        game_id = 100
        end_game = bowl_redis.EndGame(game_id)

        assert end_game.game_id == game_id

    def setup_game(self):
        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        start_game = bowl_redis.StartGame(game.game_id)
        host_player_id = game.players[0].player_id
        start_game.execute(host_player_id)

        return (game.game_id, host_player_id)

    def test_end_game_before_started(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        game_id = game.game_id
        host_player_id = game.players[0].player_id

        #verify game info exists, game info has status and status is CREATED
        #verify player is in game
        #verify player info exists, player info has status and player info status is JOINED

        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.CREATED)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.JOINED)
        
        #now end game and verify output
        end_game = bowl_redis.EndGame(game_id)
        end_game.execute(host_player_id)

        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.ABANDONED)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.ABANDONED)
    
    def test_end_game_after_started(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()

        #verify game exists, player exists, player info exists
        #verify player is in game
        #verify player info exists, player info has status and player info status is JOINED
        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.STARTED)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.DEALT)

        #now end game and verify output
        end_game = bowl_redis.EndGame(game_id)
        end_game.execute(host_player_id)

        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.FINISHED)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.FINISHED)

    def test_end_game_after_abandoned(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        game_id = game.game_id
        host_player_id = game.players[0].player_id

        #verify game info exists, game info has status and status is CREATED
        #verify player is in game
        #verify player info exists, player info has status and player info status is JOINED

        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.CREATED)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.JOINED)
        
        #now end game and verify output
        end_game = bowl_redis.EndGame(game_id)
        end_game.execute(host_player_id)

        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.ABANDONED)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.ABANDONED)

        #now end game again
        end_game = bowl_redis.EndGame(game_id)
        with pytest.raises(Exception) as err:    
            end_game.execute(host_player_id)

        assert err.value.message == 'cannot end game that is not started or created'

    def test_end_game_after_finished(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()

        #verify game exists, player exists, player info exists
        #verify player is in game
        #verify player info exists, player info has status and player info status is JOINED
        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.STARTED)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.DEALT)

        #now end game and verify output
        end_game = bowl_redis.EndGame(game_id)
        end_game.execute(host_player_id)

        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.FINISHED)
        assert helpers.verify_status_exists_in_game_info(game_id)
        assert helpers.verify_status_eq_in_game_info(game_id, GameStatus.FINISHED)

        #now end game again
        end_game = bowl_redis.EndGame(game_id)
        with pytest.raises(Exception) as err:    
            end_game.execute(host_player_id)

        assert err.value.message == 'cannot end game that is not started or created'
