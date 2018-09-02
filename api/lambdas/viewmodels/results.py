from viewmodels import PlayerModel, GameStatusModel

class ResultsModel(object):
    def __init__(self):
        self.__player_id = None
        self.__players = []
        self.__game_status = None
        self.__game_key = None
        self.__host_player_id = None

    def set_player_id(self, player_id):
        self.__player_id = player_id

    def set_players(self, players):
        self.__players = players

    def set_game_key(self, key):
        self.__game_key = key

    def set_host_player_id(self, host_player_id):
        self.__host_player_id = host_player_id

    def set_status(self, game_status):
        self.__game_status = game_status

    def json(self):

        game = {}
        game['key'] = self.__game_key
        game['hostPlayerId'] = self.__host_player_id
        game['status'] = GameStatusModel(self.__game_status).from_dto()

        results = {}
        results['playerId'] = self.__player_id
        results['players'] = [PlayerModel.from_dto(p, p.player_status == 4) for p in self.__players]
        results['game'] = game

        return results
