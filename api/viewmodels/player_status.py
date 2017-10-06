import json
from bowl_redis_dto import PlayerStatus

class PlayerStatusModel(object):
    def __init__(self, status):
        self.status = status

    def fromDto(self):
        return {'statusId': self.status, 'description': PlayerStatus.text(self.status)}
