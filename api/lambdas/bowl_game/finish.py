import bowl_redis
from bowl_redis_dto import PlayerStatus, GameStatus

class Finish(object):

    def __init__(self):
        pass

    @staticmethod
    def execute(game_id, player_id):

        finish = bowl_redis.Players(game_id, player_id)
        finish.setPlayerStatus(PlayerStatus.FINISHED)

        #need to check if there are any other players NOT in PlayerStatus.FINISHED state
        players = []

        if players.length == 0:
            game = bowl_redis.Game(game_id)
            game.setGameStatus(GameStatus.FINISHED)

        return

