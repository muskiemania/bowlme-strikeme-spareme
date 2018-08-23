import bowl_redis

class CreateDeck(object):

    def __init__(self):
        pass

    @staticmethod
    def create(game_id, number_of_decks):
        create_deck = bowl_redis.CreateDeck(game_id, number_of_decks)
        create_deck.execute()

        return None
        #return JoinGameModel(game_dto.game_id, game_dto.host_player_id, game_dto.game_key)
