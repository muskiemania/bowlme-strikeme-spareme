import jwt

class AuthToken:

    def create(**kwargs):

        _game_id = kwargs.get('game_id')
        _player_id = kwargs.get('player_id')
        _player_name = kwargs.get('player_name')
        _ttl = kwargs.get('ttl')

        _token = jwt.encode(
                payload={
                    'sub': f'{_game_id} {_player_id}',
                    'aud': 'BOWL_API',
                    'name': _player_name,
                    'exp': _ttl},
                key='secret')

        return _token

    def validate(**kwargs):

        pass


    def check(**kwargs):

        pass
