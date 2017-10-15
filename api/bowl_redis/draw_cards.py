import redis
from cards import Card, Deck
from . import RedisKeys

class DrawCards(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

        self.deck_key = RedisKeys(game_id).game_deck()
        self.discard_key = RedisKeys(game_id).game_discard()
        self.hand_key = RedisKeys(game_id, player_id).game_player_hand()


    def execute(self, number_of_cards=1):
        while number_of_cards > 0:
            pipe = self.redis.pipeline()
            pipe.rpoplpush(self.deck_key, self.hand_key)
            pipe.execute()

            pipe.llen(self.deck_key)
            [deck_size] = pipe.execute()

            if deck_size == 1:
                print 'shuffling cards!!!'
                self.__shuffle(self.discard_key, self.deck_key)

            number_of_cards = number_of_cards - 1

        return

    def __shuffle(self, source, destination):
        pipe = self.redis.pipeline()
        pipe.lrange(source, 0, -1)
        source_cards = pipe.execute()[0]
        shuffled_source = Deck.shuffle_cards(source_cards)
        for card in shuffled_source:
            pipe.lpush(destination, card)
        pipe.ltrim(source, -1, 0)
        pipe.execute()
