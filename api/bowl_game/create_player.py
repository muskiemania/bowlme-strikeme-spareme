import dynamos.create_player as dynamos
import uuid

class CreatePlayer:

    @staticmethod
    def create(game_id, player_name, is_host=False):
        
        # create a player_id
        _player_id = str(uuid.uuid4())
        
        dynamos.CreatePlayer.create(game_id, _player_id, player_name, 'joined', is_host)

        return _player_id
