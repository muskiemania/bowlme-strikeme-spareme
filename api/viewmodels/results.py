import json
from viewmodels import PlayerModel, PlayerStatusModel, GameStatusModel

class ResultsModel(object):
    def __init__(self):
        self.__players = []
        self.__game_status = None
        self.__game_key = None
        self.__host_player_id = None

    def setPlayers(self, players):
        self.__players = players

    def setGameKey(self, key):
        self.__game_key = key

    def setHostPlayerId(self, id):
        self.__host_player_id = id
        
    def setStatus(self, game_status):
        self.__game_status = game_status

    def json(self): 
        return json.dumps({'players': map(lambda x: PlayerModel.fromDto(x, x.player_status == 4), self.__players), 'game': { 'key': self.__game_key, 'hostPlayerId': self.__host_player_id, 'status': GameStatusModel(self.__game_status).fromDto()}})
