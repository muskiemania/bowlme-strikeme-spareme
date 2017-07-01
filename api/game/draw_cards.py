import bowl_redis
import game

class DrawCards(object):

    def __init__(self):
        pass

    @staticmethod
    def draw(game_id, player_id, number_of_cards=1):
        draw_cards = bowl_redis.DrawCards(game_id, player_id)
        draw_cards.execute(number_of_cards)

        return game.Game.get(game_id, player_id)
