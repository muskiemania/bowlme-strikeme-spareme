import bowl_redis
import cards
import scoring
import viewmodels

class Game(object):

    def __init__(self):
        pass

    @staticmethod
    def get(game_id, player_id=None):

        players = bowl_redis.GetPlayers(game_id)
        player_dto = players.execute()

        game_details = bowl_redis.GetGame(game_id)
        game_details_dto = game_details.execute()

        #needs:
        #all players, including name, hand, status
        #if player specified, then
        #  -- exclude "me" from players
        #  -- fetch my cards
        #  -- fetch my status
        #for the game
        #  -- need game status
        #  -- need to know if "I" am the host

        my_game = viewmodels.MyGameModel()

        if player_id is not None:
            others = [o for o in player_dto if o.player_id != player_id]
            player = [p for p in player_dto if p.player_id == player_id][0]

            my_game.setOthers(others)
            my_game.setPlayer(player)
            my_game.setStatus(game_details_dto.game_status)
            my_game.setHostPlayerId(game_details_dto.host_player_id)

        return my_game

    def sort_cards(self, unsorted):
        pass
