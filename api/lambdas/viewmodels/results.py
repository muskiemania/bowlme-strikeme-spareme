import json
from viewmodels import PlayerModel, GameStatusModel

class ResultsModel(object):
    def __init__(self):
        self.__player_id = None
        self.__players = []
        self.__game_status = None
        self.__game_key = None
        self.__host_player_id = None

    def setPlayerId(self, player_id):
        self.__player_id = player_id

    def setPlayers(self, players):
        self.__players = players

    def setGameKey(self, key):
        self.__game_key = key

    def setHostPlayerId(self, host_player_id):
        self.__host_player_id = host_player_id

    def setStatus(self, game_status):
        self.__game_status = game_status

    def json(self):

        game = {}
        game['key'] = self.__game_key
        game['hostPlayerId'] = self.__host_player_id
        game['status'] = GameStatusModel(self.__game_status).fromDto()

        results = {}
        results['playerId'] = self.__player_id
        results['players'] = [PlayerModel.fromDto(p, p.player_status == 4) for p in self.__players]
        results['game'] = game

        return json.dumps(results)
