from game import CreatePlayer
from bowl_redis_dto import PlayerStatus
import scoring

class Test_GameCreatePlayer:

    def test_createPlayer_create(self):
        playerDto = CreatePlayer.create('justin', 'key')

        assert playerDto.player_id is not None
        assert playerDto.player_name == 'justin'
        assert playerDto.player_status == None
        assert playerDto.player_rating == scoring.Scorer.default_rating().as_string()
        assert playerDto.player_rank == None
