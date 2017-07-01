import bowl_redis
import entities
import game

class DiscardCards(object):

    def __init__(self):
        pass

    @staticmethod
    def discard(game_id, player_id, cards):
        discard_cards = bowl_redis.DiscardCards(game_id, player_id)
        discard_cards.execute(cards)

        return game.Game.get(game_id, player_id)
