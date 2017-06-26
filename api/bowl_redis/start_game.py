import datetime
import redis
from cards import Deck
from entities import Game, GameStatus
from .redis_keys import RedisKeys

class StartGame(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self, host_player_id):
        key_info = RedisKeys(self.game_id)
        
        #first check to see if player id host and that status is CREATED
        pipe = self.redis.pipeline()
        pipe.hgetall(key_info.game_info())
        [info] = pipe.execute()

        if 'host_id' not in info:
            raise Exception('no host available for this game')
        if not info['host_id'] == host_player_id:
            raise Exception('only the host can start a game')
        if 'status' not in info:
            raise Exception('status unknown - cannot start this game')
        if not info['status'] == str(GameStatus.CREATED.value):
            raise Exception('cannot start a game that is not in CREATED state')

        #now start the game:
        #shuffle up and deal
        #change game status

        game = Game(self.game_id, info['host_name'])
        game.status = GameStatus.STARTED
        game.last_updated = datetime.datetime.now()
        game.deck = Deck.generate_deck()
        game.deck.shuffle_deck()

        game_info = {}
        game_info[key_info.game_info_status_key()] = game.status.value
        pipe.hmset(key_info.game_info(), info)
        pipe.rpush(key_info.game_deck(), *Deck.show_cards(game.deck.cards))

        game_updated = {}
        game_updated[key_info.game_last_updated_key()] = game.last_updated
        game_updated[key_info.game_last_updated_status_key()] = game.status.value
        pipe.hmset(key_info.game_last_updated, game_updated)

        pipe.execute()
        return game
