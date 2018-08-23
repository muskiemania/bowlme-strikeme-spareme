import redis
from cards import Deck
from .redis_keys import RedisKeys

class ShuffleDeck(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self):
        key_info = RedisKeys(self.game_id)

        #generally speaking, will always take cards from discard
        #then shuffle them
        #then re-insert them at bottom of draw pile

        #for beginning of game, all cards will be in discard pile
        #and draw pile will be empty

        #for mid game there will be many cards in discard pile
        #and draw pile will be very small

        self.__shuffle(key_info.game_discard(), key_info.game_deck())

        return None

    def __shuffle(self, source, destination):
        pipe = self.redis.pipeline()

        #get all cards from source
        pipe.lrange(source, 0, -1)
        source_cards = pipe.execute()[0]

        #shuffle cards
        shuffled_source = Deck.shuffle_cards(source_cards)

        #clear cards from source
        pipe.ltrim(source, -1, 0)

        #re-insert cards at destination
        for card in shuffled_source:
            pipe.lpush(destination, card)

        pipe.execute()
