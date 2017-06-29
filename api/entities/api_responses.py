import json

class APIGameResponse(object):
    def __init__(self):
        self.game_id = None
        self.game_status = None
        self.last_updated = None
        self.player = None
        self.players = None
        self.is_host = None
        self.cards = None

    def json(self):
        j = {}
        j['gameId'] = self.game_id
        j['gameStatus'] = self.game_status.json(dict_only=True)
        j['lastUpdated'] = self.last_updated.json(dict_only=True)

        if self.player is not None:
            j['player'] = self.player.json(dict_only=True)

        if self.players is not None:
            j['players'] = self.players.json(dict_only=True)

        if self.is_host is not None:
            j['isHost'] = self.is_host

        if self.cards is not None:
            j['cards'] = self.cards.json(dict_only=True)

        return json.dumps(j)

class APIGameStatus(object):
    def __init__(self):
        self.game_status_id = None
        self.game_status_text = None

    def json(self, dict_only=False):
        j = {}
        j['gameStatusId'] = self.game_status_id
        j['gameStatusText'] = self.game_status_text

        return dict_only and j or json.dumps(j)

class APILastUpdated(object):
    def __init__(self, datetime):
        self.month = datetime.month
        self.date = datetime.day
        self.year = datetime.year
        self.hour = datetime.hour
        self.minute = datetime.minute
        self.second = datetime.second

    def json(self, dict_only=False):
        j = {}
        j['month'] = self.month
        j['date'] = self.date
        j['year'] = self.year
        j['hour'] = self.hour
        j['minute'] = self.minute
        j['second'] = self.second

        return dict_only and j or json.dumps(j)

class APIPlayerBase(object):
    def __init__(self, player_id, player_name):
        self.player_id = player_id
        self.player_name = player_name

    def json(self, dict_only=False):
        j = {}
        j['playerId'] = self.player_id
        j['playerName'] = self.player_name

        return dict_only and j or json.dumps(j)

class APIPlayerStatus(object):
    def __init__(self):
        self.player_status_id = None
        self.player_status_text = None

    def json(self, dict_only=False):
        j = {}
        j['playerStatusId'] = self.player_status_id
        j['playerStatusText'] = self.player_status_text

        return dict_only and j or json.dumps(j)
    
class APIPlayer(APIPlayerBase):
    def __init__(self, player_id, player_name):
        APIPlayerBase.__init__(player_id, player_name)
        self.player_status = None
        self.player_score = None
        self.player_rank = None

    def json(self, dict_only=False):
        j = {}
        j['playerId'] = self.player_id
        j['playerName'] = self.player_name
        j['playerStatus'] = self.player_status.json()
        j['playerScore'] = self.player_score
        j['playerRank'] = self.player_rank

        return dict_only and j or json.dumps(j)
