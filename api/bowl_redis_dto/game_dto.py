from enum import Enum
import hashlib

class GameDto(object):
    def __init__(self):
        self.game_id = None
        self.last_updated = None
        self.host_player_name = None
        self.host_player_id = None
        self.game_status = None
        self.players = []
        self.game_key = None
        self.deck = None

    def generate_game_key(self):
        md5 = hashlib.md5()
        md5.update(self.host_player_name)
        md5.update(str(self.game_id))
        self.game_key = md5.hexdigest()[-6:]

class GameStatus(Enum):
    CREATED = 1
    STARTED = 2
    ENDED = 3
    ABANDONED = 4
    FINISHED = 5

    @classmethod
    def text(cls, status):
        t = {}
        t[1] = 'created'
        t[2] = 'started'
        t[3] = 'ended'
        t[4] = 'abandoned'
        return t[status]

    @classmethod
    def enum(cls, status):
        e = {}
        e['1'] = GameStatus.CREATED
        e['2'] = GameStatus.STARTED
        e['3'] = GameStatus.ENDED
        e['4'] = GameStatus.ABANDONED
        return e[status]
