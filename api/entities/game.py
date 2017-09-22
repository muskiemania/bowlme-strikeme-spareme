import datetime
from enum import Enum

class Game(object):
    def __init__(self, game_id, host_player_name):
        self.game_id = game_id
        self.last_updated = datetime.datetime.now()
        self.host_player = host_player_name
        self.game_status = None

        self.deck = None
        self.discard = None

        self.players = []

class GameStatus(Enum):
    CREATED = 1
    STARTED = 2
    FINISHED = 3
    ABANDONED = 4

    @classmethod
    def text(cls, status):
        t = {}
        t[1] = 'created'
        t[2] = 'started'
        t[3] = 'finished'
        t[4] = 'abandoned'
        return t[status]

    @classmethod
    def enum(cls, status):
        e = {}
        e['1'] = GameStatus.CREATED
        e['2'] = GameStatus.STARTED
        e['3'] = GameStatus.FINISHED
        e['4'] = GameStatus.ABANDONED
        return e[str(status)]
