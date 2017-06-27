import datetime
import redis
from cards import Deck
from entities import Game, GameStatus, PlayerStatus
from .redis_keys import RedisKeys
from .helpers import Helpers

class StartGame(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self, host_player_id):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()
        helpers = Helpers(pipe)

        #check to see if host_player_id is the host of the game
        if not helpers.verify_host_id_exists_in_game_info(self.game_id):
            raise Exception('no host id available for this game')
        if not helpers.verify_host_name_exists_in_game_info(self.game_id):
            raise Exception('no host name available for this game')
        if not helpers.verify_status_exists_in_game_info(self.game_id):
            raise Exception('status unknown for this game')
        if not helpers.verify_host_id_eq_in_game_info(self.game_id, host_player_id):
            raise Exception('only the host can start a game')
        
        #check to see if the game is in the proper state
        if not helpers.verify_status_eq_in_game_info(self.game_id, GameStatus.CREATED):
            raise Exception('cannot start a game that is not in CREATED status')

        # Now Start The Game
        # 1 - set game status
        # 2 - shuffle up and deal
        # 3 - set game_last_updated
        # 4 - update player_statuses

        pipe.hgetall(key_info.game_info())
        [game_info] = pipe.execute()

        game = Game(self.game_id, game_info['host_name'])
        game.game_status = GameStatus.STARTED
        game.last_updated = datetime.datetime.now()
        game.deck = Deck.generate_deck()
        game.deck.shuffle_deck()

        #1
        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), game.game_status.value)
        #2
        pipe.rpush(key_info.game_deck(), *Deck.show_cards(game.deck.cards))
        #3
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), game.last_updated)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_status_key(), game.game_status.value)

        pipe.execute()

        #4
        
        pipe.lrange(key_info.game_players(), 0, -1)
        pipe.hgetall(key_info.game_players_info())
        
        [players, players_info] = pipe.execute()

        for player_id in players:
            key_info = RedisKeys(self.game_id, player_id)
            player_status = players_info[key_info.game_players_status_key()]
            if player_status == PlayerStatus.JOINED.value:
                pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), PlayerStatus.DEALT.value)

        pipe.execute()
        
        return game
