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

    def test_start_game_execute_no_host(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        start_game = bowl_redis.StartGame(200)
        
        with pytest.raises(Exception) as exception:
            game = start_game.execute('asdfqwerty')
    
        assert exception.value.message == 'no host available for this game'

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

    def test_start_game_execute_no_info(self):
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

        assert exception.value.message == 'status unknown - cannot start this game'

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

        start_game = bowl_redis.StartGame(game.game_id)
        host_player = game.players[0]
        game = start_game.execute(host_player.player_id)
        
        #verify game status
        #verify deck
        #verify global game status

        pipe.lrange('game-%s-deck' % game.game_id, 0, -1)
        deck = pipe.execute()[0]

        print deck
        print Deck.show_cards(game.deck.cards)

        assert deck == Deck.show_cards(game.deck.cards)
