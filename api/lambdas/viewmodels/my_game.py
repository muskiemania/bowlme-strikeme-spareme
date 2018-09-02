from viewmodels import PlayerModel, GameStatusModel

class MyGameModel(object):
    def __init__(self):
        self.__player = None
        self.__others = []
        self.__game_status = None
        self.__game_key = None
        self.__host_player_id = None

    def set_player(self, player):
        self.__player = player

    def set_others(self, others):
        self.__others = others or []

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

        model = {}
        model['player'] = PlayerModel.from_dto(self.__player, True)
        model['otherPlayers'] = [PlayerModel.from_dto(o) for o in self.__others]
        model['game'] = game

        return model
