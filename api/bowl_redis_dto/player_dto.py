import hashlib
from enum import Enum
import calendar
import time

class PlayerDto(object):
    def __init__(self, player_name, game_id, player_id=None):
        if player_id is None:
            md5 = hashlib.md5()
            md5.update(player_name)
            md5.update(str(game_id))
            md5.update(str(calendar.timegm(time.gmtime())))
            self.player_id = md5.hexdigest()
        else:
            self.player_id = player_id
        self.player_name = player_name
        self.player_status = None
        self.player_score = None
        self.player_rank = None

class PlayerStatus(Enum):
    JOINED = 1
    DEALT = 2
    MUST_DISCARD = 3
    FINISHED = 4
    WINNER = 5
    ABANDONED = 6

    @classmethod
    def text(cls, status):
        print ';;;'
        print status
        print ';;;;'
        t = {}
        t[1] = 'joined'
        t[2] = 'dealt'
        t[3] = 'must discard'
        t[4] = 'finished'
        t[5] = 'winner'
        t[6] = 'abandoned'
        return t[status]

    @classmethod
    def enum(cls, status):
        e = {}
        e['1'] = PlayerStatus.JOINED
        e['2'] = PlayerStatus.DEALT
        e['3'] = PlayerStatus.MUST_DISCARD
        e['4'] = PlayerStatus.FINISHED
        e['5'] = PlayerStatus.WINNER
        e['6'] = PlayerStatus.ABANDONED
        return e[status]
