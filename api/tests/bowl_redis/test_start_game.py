from entities import GameStatus, PlayerStatus
import bowl_redis
import redis
from cards import Deck

class Test_RedisStartGame:

    def test_start_game_constructor(self):
        game_id = 200
        start_game = bowl_redis.StartGame(game_id)
        assert start_game.game_id == game_id
        
    def test_create_game_execute_no_host(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        start_game = bowl_redis.StartGame(200)
        #game = create_game.execute('asdfqwerty')

        pass

    def test_create_game_execute_not_host(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()
        
        start_game = bowl_redis.StartGame(game.game_id)
        #game = start_game.execute('Sarah')
        
        pass

    def test_create_game_execute_no_info(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        pipe.delete('game-%s-info' % game.game_id)
        pipe.execute()

        start_game = bowl_redis.StartGame(game.game_id)
        #game = start_game.execute('Justin')

        pass

    def test_create_game_execute_wrong_status(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()
        pass

        create_game = bowl_redis.CreateGame('Justin')
        game = create_game.execute()

        start_game = bowl_redis.StartGame(game.game_id)
        #start_game.execute('asdfqwerty')
        #start_game.execute('asdfqwerty')

        pass

    def test_create_game_execute(self):
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
