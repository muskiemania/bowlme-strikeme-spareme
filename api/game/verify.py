import bowl_redis
from bowl_redis_dto import GameStatus, PlayerStatus

class Verify(object):

    def __init__(self):
        pass

    @staticmethod
    def verify_game_by_key(game_key):
        #game_key is a hashed game_id
        #first see if this game exists and not ended
        verify = bowl_redis.VerifyGame()
        reply = verify.execute(game_key)

        return reply.game_status in [GameStatus.CREATED, GameStatus.STARTED]

    @staticmethod
    def verify_game_by_id(game_id):
        verify = bowl_redis.VerifyGame(game_id)
        reply = verify.execute()

        return PlayerStatus.enum(reply.game.game_status) in [GameStatus.CREATED, GameStatus.STARTED]

    @staticmethod
    def verify_player_in_game(game_id, player_id):
        verify = bowl_redis.VerifyGame(game_id, player_id)
        reply = verify.execute()

        return PlayerStatus.enum(reply.player.player_status) in [PlayerStatus.JOINED, PlayerStatus.DEALT, PlayerStatus.MUST_DISCARD]

    @staticmethod
    def get_player_status_in_game(game_id, player_id):
        verify = bowl_redis.VerifyGame(game_id, player_id)
        reply = verify.execute()
        return reply.player.player_status
