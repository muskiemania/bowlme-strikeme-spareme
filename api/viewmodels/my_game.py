import json
from viewmodels import PlayerModel, PlayerStatusModel

class MyGameModel(object):
    def __init__(self):
        self.__player = None
        self.__others = []
        self.__game_status = None

    def setPlayer(self, player):
        self.__player = player

    def setOthers(self, others):
        self.__others = others or []

    def setStatus(self, game_status):
        self.__game_status = game_status

    def json(self): 
        return json.dumps({'player': PlayerModel.fromDto(self.__player, True), 'otherPlayers': map(lambda x: PlayerModel.fromDto(x), self.__others), 'gameStatus': self.__game_status})

