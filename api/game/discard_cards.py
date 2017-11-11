import bowl_redis
from bowl_redis_dto import RatingDto
import game
import scoring
from cards import Card, Hand

class DiscardCards(object):

    def __init__(self):
        pass

    @staticmethod
    def discard(game_id, player_id, discards):
        discard_cards = bowl_redis.DiscardCards(game_id, player_id)
        cards = discard_cards.execute(discards)
        
        scorer = scoring.Scorer(Hand(map(lambda x: Card(x), cards)))
        rating_dto = RatingDto(scorer.get_rating())
        
        save_rating = bowl_redis.SetHandRating(game_id, player_id)
        save_rating.execute(rating_dto)

        #need to check player status...if 'must_discard' then must change to 'finished'
        if game.Verify.verify_player_in_game(game_id, player_id, [PlayerStatus.MUST_DISCARD]):
            players = bowl_redis.Players(game_id, player_id)
            players.setPlayerStatus(PlayerStatus.FINISHED)

        return game.Game.get(game_id, player_id)
