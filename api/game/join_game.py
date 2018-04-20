import bowl_redis
from viewmodels import JoinGameModel
from bowl_redis_dto import PlayerDto, PlayerStatus, GameStatus

class JoinGame(object):

    def __init__(self, game_key=None, game_id=None):
        self.game_id = game_id
        self.game_key = game_key

    def execute(self, player_name=None, player_id=None):
        if self.game_key is None and player_name is None:
            #verify only
            verify_game = bowl_redis.VerifyGame(self.game_id, player_id)
            verify_dto = verify_game.execute()

            if verify_dto.game.game_id == 0:
                return JoinGameModel(0, 0, '')

            game_id = verify_dto.game.game_id
            game_key = verify_dto.game.game_key
            return JoinGameModel(game_id, player_id, game_key)

        #check game then join
        verify_game = bowl_redis.VerifyGame()
        verify_dto = verify_game.execute(self.game_key)

        if verify_dto.game.game_id == 0:
            return JoinGameModel(verify_dto.game.game_id, 0, '')

        player_dto = PlayerDto(player_name, verify_dto.game.game_id)

        if verify_dto.game.game_status == GameStatus.STARTED:
            player_dto.player_status = PlayerStatus.DEALT

        create_player = bowl_redis.CreatePlayer(player_dto)
        create_player.execute(verify_dto.game.game_id)

        game_id = verify_dto.game.game_id
        player_id = player_dto.player_id
        game_key = verify_dto.game.game_key
        return JoinGameModel(game_id, player_id, game_key)
