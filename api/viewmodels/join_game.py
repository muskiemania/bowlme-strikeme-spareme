import json

class JoinGameModel(object):
    def __init__(self, game_id, player_id):
        self.__game_id = game_id
        self.__player_id = player_id

    def is_game_id_zero(self):
        return self.__game_id == 0

    def get_jwt_data(self):
        return { 'gameId': self.__game_id, 'playerId': self.__player_id }
    
    def json(self):
        return json.dumps(self.get_jwt_data())
