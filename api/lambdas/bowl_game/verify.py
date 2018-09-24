import bowl_redis
from bowl_redis_dto import GameStatus, PlayerStatus

class Verify(object):

    def __init__(self):
        pass

    @staticmethod
    def verify_game_by_key(key):

        verify = bowl_redis.VerifyGame()
        reply = verify.execute(key)

        return reply

    @staticmethod
    def verify_player_is_host(game_id, player_id):
        game_details = bowl_redis.GetGame(game_id)
        game_details_dto = game_details.execute()
        return player_id == game_details_dto.host_player_id

    #@staticmethod
    #def verify_game_by_id(game_id):

    #    verify = bowl_redis.VerifyGame(game_id)
    #    reply = verify.execute()

    #    return reply

    @staticmethod
    def verify_player_in_game(game_id, player_id, player_statuses=None):

        if player_statuses is None:
            player_statuses = [PlayerStatus.JOINED, PlayerStatus.DEALT, PlayerStatus.MUST_DISCARD, PlayerStatus.FINISHED]

        verify = bowl_redis.VerifyGame(game_id, player_id)
        reply = verify.execute()

        return PlayerStatus.enum(reply.player.player_status) in player_statuses

    @staticmethod
    def get_player_status_in_game(game_id, player_id):
        verify = bowl_redis.VerifyGame(game_id, player_id)
        reply = verify.execute()
        return reply.player.player_status
