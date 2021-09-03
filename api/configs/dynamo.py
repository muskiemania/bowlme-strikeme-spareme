import os
from enum import Enum

class DynamoConfigs(Enum):
    TABLE_NAME = f'bowlme-{os.environ["environ"]}'
