from entities import GameStatus, PlayerStatus
import bowl_redis
import redis
import pytest

class Test_RedisEndHand:

    def test_end_hand_constructor(self):
        game_id = 100
        player_id = 'asdfqwerty'
        end_hand = bowl_redis.EndHand(game_id, player_id)

        assert end_hand.game_id == game_id
        assert end_hand.player_id == player_id

    def setup_game(self):
        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        start_game = bowl_redis.StartGame(game.game_id)
        host_player_id = game.players[0].player_id
        start_game.execute(host_player_id)

        return (game.game_id, host_player_id)

    def test_end_hand_before_started(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        game_id = game.game_id
        host_player_id = game.players[0].player_id

        #verify game info exists, player exists, player info exists
        #verify player is in game
        #verify player info exists, player info has status and player info status is JOINED

        helpers = bowl_redis.Helpers(pipe)
        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.JOINED)
        
        #now end hand and verify output
        end_hand = bowl_redis.EndHand(game_id, host_player_id)
        end_hand.execute()

        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.ABANDONED)
    
    def test_end_hand_after_started(self):
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

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.DEALT)

        #now end hand and verify output
        end_hand = bowl_redis.EndHand(game_id, host_player_id)
        end_hand.execute()

        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.FINISHED)

    def test_end_hand_after_abandoned(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        game_id = game.game_id
        host_player_id = game.players[0].player_id
        end_hand = bowl_redis.EndHand(game_id, host_player_id)
        end_hand.execute()
        
        #verify game exists, player exists, player info exists
        #verify player is in game
        #verify player info exists, player info has status and player info status is ABANDONED
        helpers = bowl_redis.Helpers(pipe)

        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.ABANDONED)
                
        #now end hand again and verify output
        end_hand = bowl_redis.EndHand(game_id, host_player_id)
        with pytest.raises(Exception) as err:
            end_hand.execute()

        assert err.value.message == 'cannot end a hand for a player that is not joined or dealt'

    def test_end_hand_after_finished(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        pipe.flushall()
        pipe.execute()

        (game_id, host_player_id) = self.setup_game()
        end_hand = bowl_redis.EndHand(game_id, host_player_id)
        end_hand.execute()
        
        #verify game exists, player exists, player info exists
        #verify player is in game
        #verify player info exists, player info has status and player info status is ABANDONED
        helpers = bowl_redis.Helpers(pipe)

        assert helpers.verify_game_info_exists(game_id)
        assert helpers.verify_status_exists_in_game_info(game_id)

        assert helpers.verify_game_players_exists(game_id)
        assert helpers.verify_player_id_in_game_players(game_id, host_player_id)

        assert helpers.verify_player_info_exists(game_id, host_player_id)
        assert helpers.verify_player_status_in_player_info(game_id, host_player_id)
        assert helpers.verify_player_status_eq_in_player_info(game_id, host_player_id, PlayerStatus.FINISHED)                

        #now end hand again and verify output
        end_hand = bowl_redis.EndHand(game_id, host_player_id)
        with pytest.raises(Exception) as err:
            end_hand.execute()

        assert err.value.message == 'cannot end a hand for a player that is not joined or dealt'
