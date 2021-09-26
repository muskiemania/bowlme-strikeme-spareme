import dynamos.create_player as dynamos
import uuid
from configs.player_status import PlayerStatus

class CreatePlayer:

    @staticmethod
    def create(game_id, player_name):
        
        # create a player_id
        _player_id = str(uuid.uuid4())
        
        dynamos.CreatePlayer.create(game_id, _player_id, player_name, PlayerStatus.JOINED.value)

        return _player_id
