import redis
from cards import Deck
from .redis_keys import RedisKeys

class CreateDeck(object):

    def __init__(self, game_id, number_of_decks=1):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.number_of_decks = number_of_decks

    def execute(self):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()

        for _ in range(self.number_of_decks):
            deck = Deck.generate_deck()
            pipe.rpush(key_info.game_discard(), *Deck.show_cards(deck.cards))

        pipe.execute()
        return None
