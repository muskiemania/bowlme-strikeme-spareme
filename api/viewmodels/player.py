
from . import PlayerStatusModel, RatingModel, HandModel

class PlayerModel(object):
    def __init__(self):
        pass

    @staticmethod
    def fromDto(player, show_cards = False):

        rating = RatingModel(player.player_rating)
        status = PlayerStatusModel(player.player_status)
        hand = HandModel(player.player_cards)

        p = {'playerId': player.player_id, 'rating': rating.fromDto(), 'hand': hand.fromDto(), 'playerName': player.player_name, 'status': status.fromDto() }

        if not show_cards:
            p.pop('rating', None)
            p['hand'].pop('cards', None)

        return p
