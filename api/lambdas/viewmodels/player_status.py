from bowl_redis_dto import PlayerStatus

class PlayerStatusModel(object):
    def __init__(self, status):
        self.status = status

    def from_dto(self):
        return {'statusId': self.status, 'description': PlayerStatus.text(self.status)}
