import hashlib
import datetime
from game import CreatePlayer
import cards
import bowl_redis

# 0. need a host
# 1. need cards
# 2. need to shuffle cards
# 3. store data
# 4. return unique game id

class CreateGame(object):

    def __init__(self, game_id=0, host=None, players=None, deck=None, discard=None, status=0):
        self.game_id = game_id
        self.host = host
        self.players = players
        self.deck = deck
        self.discard = discard
        self.status = status

    def create_game_id(self, host_name=None, hash_key=datetime.datetime.now()):
        md5 = hashlib.md5()
        md5.update(host_name)
        md5.update(hash_key)
        return md5.hexdigest()

    def create(self, host_name=None, hash_key=None):
        game_id = self.create_game_id(host_name, hash_key)

        host_player = CreatePlayer(host_name, game_id)
        host = host_player.player_id

        players = {}
        players[host] = host_player.__dict__

        deck = cards.Deck()
        deck.shuffle_deck()

        discard = []

        status = 0

        return CreateGame(game_id, host, players, deck, discard, status)

    def execute(self):
        redis = bowl_redis.CreateGame()
        redis.init(self)

        if redis.execute():
            return self.game_id
