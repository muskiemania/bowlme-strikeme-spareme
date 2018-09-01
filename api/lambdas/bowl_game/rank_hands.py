import bowl_redis
import scoring

class RankHands(object):

    def __init__(self):
        pass

    @staticmethod
    def rank(game_id):

        get_ratings = bowl_redis.GetHandRatings(game_id)
        all_ratings = get_ratings.execute()

        ranked = scoring.Scorer.rank_hands(all_ratings)

        save_rankings = bowl_redis.SetHandRankings(game_id)
        save_rankings.execute(ranked)

        return
