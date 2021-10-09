import os
from enum import Enum

class SnsConfigs(Enum):
    SCORING_TOPIC_ARN = 'arn:aws:sns:us-west-2:359299993558:bowlme-v2-us-west-2-scoring'

    def __str__(self):
        return '%s' % self.value
