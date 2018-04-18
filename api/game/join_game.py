import bowl_redis
from viewmodels import JoinGameModel
from bowl_redis_dto import PlayerDto

class JoinGame(object):

    def __init__(self, game_key=None, game_id=None):
        self.game_id = game_id
        self.game_key = game_key

    def execute(self, player_name=None, player_id=None):
        if self.game_key is None and player_name is None:
            #verify only
            verify = bowl_redis.VerifyGame(self.game_id, player_id)
            dto = verify.execute()

            if dto.game.game_id == 0:
                return JoinGameModel(0, 0, '')

            return JoinGameModel(dto.game.game_id, player_id, dto.game.game_key)

        #check game then join
        verify = bowl_redis.VerifyGame()
        verify_dto = verify.execute(self.game_key)

        print verify_dto.__dict__

        if verify_dto.game.game_id == 0:
            return JoinGameModel(verify_dto.game_id, 0, '')

        player_dto = PlayerDto(player_name, verify_dto.game.game_id)
        create_player = bowl_redis.CreatePlayer(player_dto)
        create_player.execute(verify_dto.game.game_id)

        return JoinGameModel(verify_dto.game.game_id, player_dto.player_id, verify_dto.game.game_key)
