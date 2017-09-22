import bowl_redis

class Verify(object):

    def __init__(self):
        pass

    @staticmethod
    def verify(game_key, player_key):
        #game_key is a hashed game_id
        #first see if this game exists and not ended
        getGameId = bowl_redis.GetGameIdByHash()
        reply = getGameId.execute(game_key)
        
        if not reply:
            return None

        #now check game status
        getGameStatus = bowl_redis.GetGameStatusByGameId()
        reply = getGameStatus.execute(reply.game_id)

        if not reply:
            return None
        if reply.game_status not in (GameStatus.CREATED, GameStatus.STARTED):
            return None
        
        #player_key is a hashed player_name-game_id
        getPlayerId = bowl_redis.GetPlayerByHash()
        reply = getPlayerId.execute(game_id, player_key)

        if not reply:
            return None
        
        #now check player status
        getPlayerStatus = bowl_redis.GetPlayerStatus(game_id)
        reply = getPlayerStatus.execute(reply.player_id)

        if not reply:
            return None
        if reply.player_status not in (PlayerStatus.JOINED, PlayerStatus.DEALT):
            return None
        
        return { game_id, player_id, game_key, player_key }
