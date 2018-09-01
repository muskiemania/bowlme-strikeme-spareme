import bowl_redis

class DrawCards(object):

    def __init__(self):
        pass

    @staticmethod
    def draw(game_id, player_id, number_of_cards=1):

        #first draw cards
        draw_cards = bowl_redis.DrawCards(game_id, player_id)
        cards = None

        if number_of_cards > 0:
            cards = draw_cards.execute(number_of_cards)

        return {
            cards: cards,
            number_of_cards: number_of_cards
        }

#        if number_of_cards in [3, 4, 6]:
#            players = bowl_redis.Players(game_id, player_id)
#            if len(cards) > 5:
#                players.setPlayerStatus(PlayerStatus.MUST_DISCARD)
#            else:
#                players.setPlayerStatus(PlayerStatus.FINISHED)
