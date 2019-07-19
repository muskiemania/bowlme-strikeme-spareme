from bowl_redis import RedisKeys
from bowl_redis_dto import GameStatus, PlayerStatus
from cards import Deck
import datetime

class Helpers(object):
    def __init__(self, pipe):
        self.pipe = pipe

    def __key_exists(self, hash_key):
        self.pipe.exists(hash_key)
        [exists] = self.pipe.execute()
        return exists

    def __key_exists_within_hash(self, hash_key, lookup):
        self.pipe.hexists(hash_key, lookup)
        [exists] = self.pipe.execute()
        return exists

    def __value_eq_within_hash(self, hash_key, lookup, value):
        self.pipe.hget(hash_key, lookup)
        [result] = self.pipe.execute()

        if isinstance(value, datetime.datetime):
            return result == str(value)
        if isinstance(value, GameStatus) or isinstance(value, PlayerStatus):
            return result == value
        if isinstance(value, str):
            return result == value
        if isinstance(value, int):
            return result == str(value)
        if isinstance(value, tuple):
            return result == value

    def __value_exists_within_list(self, list_key, value):
        self.pipe.lrange(list_key, 0, -1)
        [items] = self.pipe.execute()
        return value in items

    #game-[game_id]-info: a hash of info specific to a single game
    def verify_game_info_exists(self, game_id):
        key_info = RedisKeys(game_id)
        return self.__key_exists(key_info.game_info())

    def verify_host_name_exists_in_game_info(self, game_id):
        key_info = RedisKeys(game_id)
        host_name_key = key_info.game_info_host_name_key()
        return self.__key_exists_within_hash(key_info.game_info(), host_name_key)

    def verify_host_id_exists_in_game_info(self, game_id):
        key_info = RedisKeys(game_id)
        return self.__key_exists_within_hash(key_info.game_info(), key_info.game_info_host_id_key())

    def verify_status_exists_in_game_info(self, game_id):
        key_info = RedisKeys(game_id)
        return self.__key_exists_within_hash(key_info.game_info(), key_info.game_info_status_key())

    def verify_host_name_eq_in_game_info(self, game_id, host_name):
        key_info = RedisKeys(game_id)
        host_name_key = key_info.game_info_host_name_key()
        return self.__value_eq_within_hash(key_info.game_info(), host_name_key, host_name)

    def verify_host_id_eq_in_game_info(self, game_id, host_id):
        key_info = RedisKeys(game_id)
        host_id_key = key_info.game_info_host_id_key()
        return self.__value_eq_within_hash(key_info.game_info(), host_id_key, host_id)

    def verify_status_eq_in_game_info(self, game_id, status):
        key_info = RedisKeys(game_id)
        game_status_key = key_info.game_info_status_key()
        return self.__value_eq_within_hash(key_info.game_info(), game_status_key, status)

    #game-[game_id]-players: a list of all player_ids in a single game
    def verify_game_players_exists(self, game_id):
        key_info = RedisKeys(game_id)
        return self.__key_exists(key_info.game_players())

    def verify_player_id_in_game_players(self, game_id, player_id):
        key_info = RedisKeys(game_id, player_id)
        return self.__value_exists_within_list(key_info.game_players(), player_id)

    #game-[game_id]-players-info: a hash of specific info for all players in a single game
    def verify_player_info_exists(self, game_id, player_id):
        key_info = RedisKeys(game_id, player_id)
        print(key_info.__dict__)
        print(key_info.game_players_info())
        return self.__key_exists(key_info.game_players_info())

    def verify_player_name_in_player_info(self, game_id, player_id):
        key_info = RedisKeys(game_id, player_id)
        players_name_key = key_info.game_players_name_key()
        return self.__key_exists_within_hash(key_info.game_players_info(), players_name_key)

    def verify_player_status_in_player_info(self, game_id, player_id):
        key_info = RedisKeys(game_id, player_id)
        players_status_key = key_info.game_players_status_key()
        return self.__key_exists_within_hash(key_info.game_players_info(), players_status_key)

    def verify_player_name_eq_in_player_info(self, game_id, player_id, player_name):
        key_info = RedisKeys(game_id, player_id)
        players_info = key_info.game_players_info()
        players_name_key = key_info.game_players_name_key()
        return self.__value_eq_within_hash(players_info, players_name_key, player_name)

    def verify_player_status_eq_in_player_info(self, game_id, player_id, player_status):
        key_info = RedisKeys(game_id, player_id)
        players_info = key_info.game_players_info()
        players_status_key = key_info.game_players_status_key()
        return self.__value_eq_within_hash(players_info, players_status_key, player_status)

    def verify_player_rating_eq_in_player_info(self, game_id, player_id, player_rating):
        key_info = RedisKeys(game_id, player_id)
        players_info = key_info.game_players_info()
        players_rating_key = key_info.game_players_rating()
        return self.__value_eq_within_hash(players_info, players_rating_key, player_rating)

    def verify_player_ranking_eq_in_player_info(self, game_id, player_id, player_ranking):
        key_info = RedisKeys(game_id, player_id)
        players_info = key_info.game_players_info()
        players_ranking_key = key_info.game_players_rank()
        return self.__value_eq_within_hash(players_info, players_ranking_key, player_ranking)

    #game_last_updated: a hash of all games, last updated and status
    def verify_game_last_updated_exists(self):
        key_info = RedisKeys()
        return self.__key_exists(key_info.game_last_updated())

    def verify_game_updated_exists(self, game_id):
        key_info = RedisKeys(game_id)
        last_updated_key = key_info.game_last_updated_key()
        return self.__key_exists_within_hash(key_info.game_last_updated(), last_updated_key)

    def verify_game_status_exists(self, game_id):
        key_info = RedisKeys(game_id)
        last_updated_status_key = key_info.game_last_updated_status_key()
        return self.__key_exists_within_hash(key_info.game_last_updated(), last_updated_status_key)

    def verify_game_updated_eq_in_game_last_updated(self, game_id, last_updated):
        key_info = RedisKeys(game_id)
        game_last_updated = key_info.game_last_updated()
        last_updated_key = key_info.game_last_updated_key()
        return self.__value_eq_within_hash(game_last_updated, last_updated_key, last_updated)

    def verify_game_status_eq_in_game_last_updated(self, game_id, status):
        key_info = RedisKeys(game_id)
        game_last_updated = key_info.game_last_updated()
        last_updated_status_key = key_info.game_last_updated_status_key()
        return self.__value_eq_within_hash(game_last_updated, last_updated_status_key, status)

    #game-[game_id]-deck: a list of all cards
    def verify_game_deck_exists(self, game_id):
        key_info = RedisKeys(game_id)
        return self.__key_exists(key_info.game_deck())

    def verify_game_deck_is_valid(self, game_id, number_of_cards=None):
        key_info = RedisKeys(game_id)
        deck = Deck.generate_deck()
        cards = Deck.show_cards(deck.cards)
        for card in cards:
            if not self.__value_exists_within_list(key_info.game_deck(), card):
                return False
        return True
