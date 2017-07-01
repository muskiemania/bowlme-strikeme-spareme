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
            j['players'] = [player.json(dict_only=True) for player in self.players]

        if self.is_host is not None:
            j['isHost'] = self.is_host

        if self.cards is not None:
            j['cards'] = [card.json(dict_only=True) for card in self.cards]

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
        APIPlayerBase.__init__(self, player_id, player_name)
        self.player_status = None
        self.player_rank = None

    def json(self, dict_only=False):
        j = {}
        j['playerId'] = self.player_id
        j['playerName'] = self.player_name
        j['playerStatus'] = self.player_status.json(dict_only)

        rating = self.hand_rating.json(dict_only)
        if rating:
            j['handRating'] = rating
        
        j['playerRank'] = self.player_rank

        return dict_only and j or json.dumps(j)

class APICard(object):
    def __init__(self, card):
        self.card = { 'card': card.card, 'display': card.card_display }
        self.suit = { 'suit': card.suit, 'suitName': card.suit_name }

    def json(self, dict_only=False):
        card = {}
        card['card'] = self.card
        card['suit'] = self.suit
        return dict_only and card or json.dumps(card)

class APIHandRating(object):
    def __init__(self, rating, show_cards):
        self.rating = rating
        self.show_cards = show_cards

    def get_null_rating(self):
        rating = list(self.rating)[1:]
        return ['X' for card in rating if card is not 0]
        
    def json(self, dict_only=False):

        if not self.show_cards:
            null_rating = self.get_null_rating()
            return dict_only and null_rating or json.dumps(null_rating)
        
        rating = {}
        rating['handType'] = 'TODO: rating here'
        rating['cards'] = list(self.rating)[1:]
        return dict_only and rating or json.dumps(rating)
        
