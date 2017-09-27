import json

class MyGameModel(object):
    def __init__(self):
        self.__players = []
        self.__my_cards = []
        self.__game_status = None
        self.__player_status = None

    def setPlayers(self, players):
        self.__players = players

    def setCards(self, cards):
        self.__cards = cards

    def setStatus(self, game_status=None, player_status=None):
        if game_status is not None:
            self.__game_status = game_status

        if player_status is not None:
            self.__player_status = player_status
        
    def json(self):
        return json.dumps({'players': self.__players,
                           'myCards': self.__my_cards,
                           'gameStatus': self.__game_status,
                           'playerStatus': self.__player_status})
