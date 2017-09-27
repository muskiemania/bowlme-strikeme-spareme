import bowl_redis
import entities
import cards
import scoring

class Game(object):

    def __init__(self):
        pass

    @staticmethod
    def get(game_id, player_id=None):

        players = bowl_redis.GetPlayers(game_id)
        player_dto = players.execute()

        game_details = bowl_redis.GetGameDetails(game_id)
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

        cards = []
        
        if player_id is not None:
            player_dto = filter(lambda x: x.player_id != player_id, player_dto)
            me = filter(lambda x: x.player_id == player_id)
            cards = me.cards

        my_game = MyGameModel()
        my_game.setPlayers(player_dto)
        my_game.setCards(cards)
        my_game.setStatus(player_status=me.status)
        my_game.setStatus(game_status=game_details_dto.game_status)
            
        return my_game.json()
