from entities import Player, PlayerStatus
import bowlRedis
import redis

class Test_RedisCreatePlayer:

    def test_create_player_constructor(self):
        game_id = 100
        player = Player('Justin', game_id)
        create_player = bowlRedis.CreatePlayer(player)
        
        assert create_player.player == player
        assert create_player.player.player_status == PlayerStatus.JOINED
        
    def test_create_player_execute(self):
        r = redis.StrictRedis()
        pipe = r.pipeline()
        r.flushall()
        pipe.execute()

        game_id = 100
        player = Player('Justin', game_id)
        create_player = bowlRedis.CreatePlayer(player)
        create_player.execute(game_id)

        player_exists = pipe.exists('game-%s-players' % game_id).execute()[0]
        player_name = pipe.hgetall('game-%s-players' % game_id).execute()[0]
        player_status_exists = pipe.exists('game-%s-player-statuses' % game_id).execute()[0]
        player_statuses = pipe.hgetall('game-%s-player-statuses' % game_id).execute()[0]
