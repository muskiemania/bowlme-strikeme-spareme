from enum import Enum

class GameDto(object):
    def __init__(self):
        self.game_id = None
        self.last_updated = None
        self.host_player_name = None
        self.host_player_id = None
        self.game_status = None
        self.players = []

class GameStatus(Enum):
    CREATED = 1
    STARTED = 2
    ENDED = 3
    ABANDONED = 4

    @classmethod
    def text(cls, status):
        t = {}
        t[1] = 'created'
        t[2] = 'started'
        t[3] = 'ended'
        t[4] = 'abandoned'
        return t[status.value]

    @classmethod
    def enum(cls, status):
        e = {}
        e['1'] = PlayerStatus.JOINED
        e['2'] = PlayerStatus.DEALT
        e['3'] = PlayerStatus.FINISHED
        e['4'] = PlayerStatus.WINNER
        return e[status]
