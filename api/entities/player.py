import hashlib
from enum import Enum
import calendar
import time

class Player(object):
    def __init__(self, player_name, game_id):
        md5 = hashlib.md5()
        md5.update(player_name)
        md5.update(str(game_id))
        md5.update(str(calendar.timegm(time.gmtime())))
        self.player_name = player_name
        self.player_id = md5.hexdigest()
        self.player_status = None

class PlayerStatus(Enum):
    JOINED = 1
    DEALT = 2
    FINISHED = 3
    WINNER = 4
    ABANDONED = 5

    @classmethod
    def text(cls, status):
        t = {}
        t[1] = 'joined'
        t[2] = 'dealt'
        t[3] = 'finished'
        t[4] = 'winner'
        t[5] = 'abandoned'
        return t[status.value]
