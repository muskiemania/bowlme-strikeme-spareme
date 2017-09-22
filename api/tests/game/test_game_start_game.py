from game import StartGame, CreateGame
from bowl_redis_dto import GameStatus

class Test_GameStartGame:

    def _test_startGameConstructor_noArgs(self):
        sg = StartGame()

        assert sg.game_id == 0
        assert sg.player_id == None

    def test_startGameStart(self):
        gameDto = CreateGame.create('justin')

        startedGameDto = StartGame.start(gameDto.game_id, gameDto.host_player_id)

        assert startedGameDto.game_status == GameStatus.STARTED
