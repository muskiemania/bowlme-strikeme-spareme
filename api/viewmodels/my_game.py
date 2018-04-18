import json
from viewmodels import PlayerModel, GameStatusModel

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

        game = {}
        game['key'] = self.__game_key
        game['hostPlayerId'] = self.__host_player_id
        game['status'] = GameStatusModel(self.__game_status).fromDto()

        model = {}
        model['player'] = PlayerModel.fromDto(self.__player, True)
        model['otherPlayers'] = map(lambda x: PlayerModel.fromDto(x), self.__others)
        model['game'] = game

        return json.dumps(model)

