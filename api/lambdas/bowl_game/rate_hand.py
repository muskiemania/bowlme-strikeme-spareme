import bowl_redis
from cards import Card, Hand
import scoring

class RateHand(object):

    def __init__(self):
        pass

    @staticmethod
    def rate(game_id, player_id, cards):

        scorer = scoring.Scorer(Hand(Card(x) for x in cards))
        rating_dto = scorer.get_rating()

        save_rating = bowl_redis.SetHandRating(game_id, player_id)
        save_rating.execute(rating_dto)

        return
