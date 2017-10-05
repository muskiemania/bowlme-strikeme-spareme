import bowl_redis
import entities
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
            player_dto = filter(lambda x: x.player_id != player_id, player_dto)
            my_game.setPlayers(player_dto)

            me = filter(lambda x: x.player_id == player_id, player_dto)
            print player_id
            print player_dto
            if len(me) == 1:
                me = me[0]
                my_game.setCards(me.cards)
                my_game.setStatus(player_status=me.player_status)

            my_game.setStatus(game_status=game_details_dto.game_status)
            
        return my_game
