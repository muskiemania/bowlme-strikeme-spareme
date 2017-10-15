import datetime
import redis
from cards import Deck
from bowl_redis_dto import GameDto, GameStatus, PlayerStatus
from .redis_keys import RedisKeys
from .helpers import Helpers

class StartGame(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()
        helpers = Helpers(pipe)

        # To Start The Game
        # 1 - set game status
        # 2 - shuffle up and deal
        # 3 - set game_last_updated
        # 4 - update player_statuses

        pipe.hgetall(key_info.game_info())
        [game_info] = pipe.execute()

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
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), game_dto.last_updated)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_status_key(), game_dto.game_status)
        pipe.execute()

        #4
        pipe.lrange(key_info.game_players(), 0, -1)
        pipe.hgetall(key_info.game_players_info())
        [players, players_info] = pipe.execute()

        for player_id in players:
            key_info = RedisKeys(self.game_id, player_id)
            player_status = players_info[key_info.game_players_status_key()]
            
            if player_status == str(PlayerStatus.JOINED):
                pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), PlayerStatus.DEALT)
        pipe.execute()
        
        return
