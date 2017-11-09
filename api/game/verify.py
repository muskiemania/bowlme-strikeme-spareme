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
    def verify_player_is_host(game_id, player_id):
        game_details = bowl_redis.GetGame(game_id)
        game_details_dto = game_details.execute()
        return player_id == game_details_dto.host_player_id
    
    @staticmethod
    def verify_game_by_id(game_id, game_statuses = [GameStatus.CREATED, GameStatus.STARTED]):
        verify = bowl_redis.VerifyGame(game_id)
        reply = verify.execute()

        #print 'ee'
        #print reply.game.game_status
        
        #print game_statuses
        #print GameStatus.enum(reply.game.game_status) in game_statuses
        #print 'ff'
        
        return GameStatus.enum(reply.game.game_status) in game_statuses

    @staticmethod
    def verify_player_in_game(game_id, player_id, player_statuses = [PlayerStatus.JOINED, PlayerStatus.DEALT, PlayerStatus.MUST_DISCARD, PlayerStatus.FINISHED]):
        verify = bowl_redis.VerifyGame(game_id, player_id)
        reply = verify.execute()

        return PlayerStatus.enum(reply.player.player_status) in player_statuses

    @staticmethod
    def get_player_status_in_game(game_id, player_id):
        verify = bowl_redis.VerifyGame(game_id, player_id)
        reply = verify.execute()
        return reply.player.player_status
