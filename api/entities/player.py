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

class PlayerStatus(Enum):
    JOINED = 0
    DEALT = 1
    FINISHED = 2
    WINNER = 3
