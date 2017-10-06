import json
from bowl_redis_dto import PlayerDto, PlayerStatus

class PlayerModel(object):
    def __init__(self):
        pass

    @staticmethod
    def fromDto(players):
        return map(lambda x: {'playerId': x.player_id, 'score': x.player_score, 'rank': x.player_rank, 'playerName': x.player_name, 'status': x.player_status}, players)
