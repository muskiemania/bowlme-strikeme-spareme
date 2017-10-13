import json
from bowl_redis_dto import PlayerDto, PlayerStatus
from . import PlayerStatusModel

class PlayerModel(object):
    def __init__(self):
        pass

    @staticmethod
    def fromDto(player, show_cards = False):
        
        p = {'playerId': player.player_id, 'score': player.player_score, 'hand': { 'cards': player.player_cards, 'numberOfCards': len(player.player_cards)}, 'rank': player.player_rank, 'playerName': player.player_name, 'status': PlayerStatusModel(player.player_status).fromDto() }

        if not show_cards:
            p['hand'].pop('cards', None)

        return p
