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
    CREATED = 0
    STARTED = 1
    FINISHED = 2
    ABANDONED = 3
