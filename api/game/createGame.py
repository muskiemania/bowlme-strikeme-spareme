import hashlib
import datetime
from createPlayer import CreatePlayer
import cards
import bowlRedis

# 0. need a host
# 1. need cards
# 2. need to shuffle cards
# 3. store data
# 4. return unique game id

class CreateGame:

    def __init__(self, game_id = 0, host = None, players = None, deck = None, discard = None, status = 0):
        self.game_id = game_id
        self.host = host
        self.players = players
        self.deck = deck
        self.discard = discard
        self.status = status

    def create_game_id(self, host_name = None, hash_key = datetime.datetime.now()):
        m = hashlib.md5()
        m.update(host_name)
        m.update(hash_key)
        return m.hexdigest()
        
    def create(self, host_name = None, hash_key = None):
        game_id = self.create_game_id(host_name, hash_key) 
        
        host_player = CreatePlayer(host_name, game_id)
        
        host = host_player.player_id

        players = {}
        players[host] = host_player.__dict__

        deck = cards.Deck()
        deck.shuffle_deck()

        discard = []

        status = 0

        return CreateGame(game_id=game_id,host=host,players=players,deck=deck,discard=discard,status=status)

    def Exec(self):
        r = bowlRedis.CreateGame()
        r.init(self)
        
        if r.Exec():
            return self.game_id
