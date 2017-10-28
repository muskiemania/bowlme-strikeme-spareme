import json
from bowl_redis_dto import PlayerDto, PlayerStatus
from . import PlayerStatusModel, HandRatingModel

class PlayerModel(object):
    def __init__(self):
        pass

    @staticmethod
    def fromDto(player, show_cards = False):
        
        p = {'playerId': player.player_id, 'rating': HandRatingModel(player.player_rating).fromDto(), 'hand': { 'cards': player.player_cards, 'numberOfCards': len(player.player_cards)}, 'rank': player.player_rank, 'playerName': player.player_name, 'status': PlayerStatusModel(player.player_status).fromDto() }

        if not show_cards:
            p.pop('rating', None)
            p['hand'].pop('cards', None)

        return p
