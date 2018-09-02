import os
import redis
from cards import Deck
from .redis_keys import RedisKeys

class CreateDeck(object):

    def __init__(self, game_id, number_of_decks=1):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
        self.game_id = game_id
        self.number_of_decks = number_of_decks

    def execute(self):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()

        for _ in range(self.number_of_decks):
            deck = Deck.generate_deck()
            pipe.rpush(key_info.game_discard(), *Deck.show_cards(deck.cards))

        pipe.execute()
        return {'gameId': self.game_id}
