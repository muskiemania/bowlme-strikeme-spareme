import bowl_redis
from bowl_redis_dto import PlayerStatus
from cards import Card, Hand
import scoring

class DrawCards(object):

    def __init__(self):
        pass

    @staticmethod
    def draw(game_id, player_id, number_of_cards=1):

        #first draw cards
        draw_cards = bowl_redis.DrawCards(game_id, player_id)

        if number_of_cards > 0:
            cards = draw_cards.execute(number_of_cards)

            #if total number of cards is 5 then score the hand
            if len(cards) <= 5:
                scorer = scoring.Scorer(Hand(map(lambda x: Card(x), cards)))
                rating_dto = scorer.get_rating()

                save_rating = bowl_redis.SetHandRating(game_id, player_id)
                save_rating.execute(rating_dto)

                get_ratings = bowl_redis.GetHandRatings(game_id)
                all_ratings = get_ratings.execute()

                ranked = scoring.Scorer.rank_hands(all_ratings)

                save_rankings = bowl_redis.SetHandRankings(game_id)
                save_rankings.execute(ranked)

        #if cards is 3, 4 or 6:
        # - player status will change to must discard or finished
        # - if number of cards in hand is 5 or less, go straight to finished
        # - else go to must discard
        if number_of_cards in [3, 4, 6]:
            players = bowl_redis.Players(game_id, player_id)
            if len(cards) > 5:
                players.setPlayerStatus(PlayerStatus.MUST_DISCARD)
            else:
                players.setPlayerStatus(PlayerStatus.FINISHED)

        return
