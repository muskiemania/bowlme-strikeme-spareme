from . import PlayerStatusModel, RatingModel, HandModel

class PlayerModel(object):
    def __init__(self):
        pass

    @staticmethod
    def from_dto(player_dto, show_cards=False):

        rating = RatingModel(player_dto.player_rating)
        status = PlayerStatusModel(player_dto.player_status)
        hand = HandModel(player_dto.player_cards)

        player = {'playerId': player_dto.player_id,
                  'rating': rating.fromDto(),
                  'hand': hand.fromDto(),
                  'playerName': player_dto.player_name,
                  'status': status.from_dto()}

        if not show_cards:
            player.pop('rating', None)
            player['hand'].pop('cards', None)

        return player
