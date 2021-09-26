import os
from enum import Enum

class DynamoConfigs(Enum):
    GAME_TABLE_NAME = f'bowlme-game-{os.environ["environ"]}'
    PLAYER_TABLE_NAME = f'bowlme-player-{os.environ["environ"]}'
    LEADERBOARD_TABLE_NAME = f'bowlme-leaderboard-{os.environ["environ"]}'
    DECK = 'deck',
    DISCARD = 'discard'

    def __str__(self):
        return '%s' % self.value
