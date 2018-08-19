import datetime
import redis
from cards import Deck
from scoring import Scorer
from bowl_redis_dto import GameDto, GameStatus, PlayerStatus
from .redis_keys import RedisKeys
from .helpers import Helpers

class StartGame(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.__default_rating = Scorer.default_rating()

    def execute(self):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()

        # To Start The Game
        # 1 - set game status
        # 2 - shuffle up and deal
        # 3 - set game_last_updated
        # 4 - update player_statuses

        game_dto = GameDto()
        game_dto.game_id = self.game_id
        game_dto.game_status = GameStatus.STARTED
        game_dto.last_updated = datetime.datetime.now()
        game_dto.deck = Deck.generate_deck()
        game_dto.deck.shuffle_deck()

        #1
        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), game_dto.game_status)
        #2
        pipe.rpush(key_info.game_deck(), *Deck.show_cards(game_dto.deck.cards))
        #3
        last_updated = key_info.game_last_updated()
        updated_key = key_info.game_last_updated_key()
        game_status_key = key_info.game_last_updated_status_key()
        pipe.hset(last_updated, updated_key, game_dto.last_updated)
        pipe.hset(last_updated, game_status_key, game_dto.game_status)
        pipe.execute()

        #4
        pipe.lrange(key_info.game_players(), 0, -1)
        pipe.hgetall(key_info.game_players_info())
        [players, players_info] = pipe.execute()

        for player_id in players:
            key_info = RedisKeys(self.game_id, player_id)

            players_info_key = key_info.game_players_info()
            players_status_key = key_info.game_players_status_key()
            rating_key = key_info.game_players_rating()
            rank_key = key_info.game_players_rank()

            player_status = players_info[players_status_key]

            if player_status == str(PlayerStatus.JOINED):
                pipe.hset(players_info_key, players_status_key, PlayerStatus.DEALT)
                pipe.hset(players_info_key, rating_key, self.__default_rating.as_string())
                pipe.hset(players_info_key, rank_key, self.__default_rating.rank)
                print 'applied default rating ' + self.__default_rating.as_string()
                print 'applied default ranking ' + str(self.__default_rating.rank)
                pipe.execute()

        return
