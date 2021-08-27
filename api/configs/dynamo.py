import os
from enum import Enum

class DynamoConfigs(Enum)
    TABLE_NAME = f'bowl-table-{os.environ["environ"]}'
