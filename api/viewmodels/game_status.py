import json
from bowl_redis_dto import GameStatus

class GameStatusModel(object):
    def __init__(self, status):
        self.status = status

    def fromDto(self):
        return {'statusId': self.status, 'description': GameStatus.text(self.status)}
