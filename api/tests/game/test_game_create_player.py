from game import CreatePlayer
from bowl_redis_dto import PlayerStatus

class Test_GameCreatePlayer:

    def test_createPlayer_create(self):
        playerDto = CreatePlayer.create('justin', 'key')

        assert playerDto.player_id is not None
        assert playerDto.player_name == 'justin'
        assert playerDto.player_status == PlayerStatus.JOINED
        assert playerDto.player_score == None
        assert playerDto.player_rank == None
