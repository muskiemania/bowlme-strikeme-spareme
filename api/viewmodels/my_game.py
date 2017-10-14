import json
from viewmodels import PlayerModel, PlayerStatusModel, GameStatusModel

class MyGameModel(object):
    def __init__(self):
        self.__player = None
        self.__others = []
        self.__game_status = None
        self.__game_key = None
        self.__host_player_id = None

    def setPlayer(self, player):
        self.__player = player

    def setOthers(self, others):
        self.__others = others or []

    def setGameKey(self, key):
        self.__game_key = key

    def setHostPlayerId(self, id):
        self.__host_player_id = id
        
    def setStatus(self, game_status):
        self.__game_status = game_status

    def json(self): 
        return json.dumps({'player': PlayerModel.fromDto(self.__player, True), 'otherPlayers': map(lambda x: PlayerModel.fromDto(x), self.__others), 'game': { 'key': self.__game_key, 'hostPlayerId': self.__host_player_id, 'status': GameStatusModel(self.__game_status).fromDto()}})

