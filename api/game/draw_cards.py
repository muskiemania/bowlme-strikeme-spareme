import bowl_redis
from bowl_redis_dto import PlayerStatus, RatingDto
import game
from cards import Card, Hand
import scoring

class DrawCards(object):

    def __init__(self):
        pass

    @staticmethod
    def draw(game_id, player_id, number_of_cards=1):

        #first draw cards
        draw_cards = bowl_redis.DrawCards(game_id, player_id)
        cards = draw_cards.execute(number_of_cards)

        #if total number of cards is 5 then score the hand
        if len(cards) <= 5:
            scorer = scoring.Scorer(Hand(map(lambda x: Card(x), cards)))
            rating_dto = RatingDto(scorer.get_rating())

            save_rating = bowl_redis.SetHandRating(game_id, player_id)
            save_rating.execute(rating_dto)

        #if cards is 3, 4 or 6:
        # - player status will change to must discard or finished
        # - if number of cards in hand is 5 or less, go straight to finished
        # - else go to must discard
        if number_of_cards > 2:
            print 'cards > 2'
            if len(cards) > 5:
                print 'len > 5: must_discard'
                draw_cards.changePlayerStatus(PlayerStatus.MUST_DISCARD)
            else:
                print 'finished'
                draw_cards.changePlayerStatus(PlayerStatus.FINISHED)

        print 'done'
        return
