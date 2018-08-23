import bowl_redis

class DiscardCards(object):

    def __init__(self):
        pass

    @staticmethod
    def discard(game_id, player_id, discards):
        discard_cards = bowl_redis.DiscardCards(game_id, player_id)
        cards = discard_cards.execute(discards)

        return {
            cards: cards
        }
