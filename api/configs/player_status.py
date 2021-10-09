from enum import Enum

class PlayerStatusConfigs(Enum):
    JOINED = 'joined'
    FINISHED = 'finished'
    DEALT = 'dealt'
    MUST_DISCARD = 'must_discard'
    FINISHED_MUST_DISCARD = 'finished_must_discard'


